
from rest_framework import generics
from .models import Story, UserPrompt
from .serializers import StorySerializer, UserPromptSerializer
import openai
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserPromptSerializer

class StoryListCreateView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class UserPromptCreateView(generics.CreateAPIView):
    queryset = UserPrompt.objects.all()
    serializer_class = UserPromptSerializer


class StoryListCreateView(APIView):
    # Existing code

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate story using GPT-3.5
        prompt = serializer.validated_data['prompt']
        generated_story = self.generate_story(prompt)

        # Save the generated story to the database
        Story.objects.create(prompt=prompt, content=generated_story)

        return Response({'story': generated_story}, status=status.HTTP_201_CREATED)

    def generate_story(self, prompt):
        # Use the OpenAI API to generate the story
        # Replace 'YOUR_API_KEY' with your actual API key
        openai.api_key = 'YOUR_API_KEY'

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )

        return response['choices'][0]['text'].strip()


