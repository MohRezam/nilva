from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.mock_data import get_mock_data
from .serializers import WeatherSerializer
import logging


logger = logging.getLogger(__name__)

class WeatherAPIView(APIView):
    """
    API View for retrieving weather information.

    This view retrieves mock weather data using `get_mock_data` function,
    serializes it using `WeatherSerializer`, and returns the serialized data
    if valid. If serialization fails, it returns the serialization errors.

    Attributes:
        serializer_class (WeatherSerializer): Serializer class for weather data.

    Methods:
        get(request):
            Retrieves mock weather data, validates it using `WeatherSerializer`,
            and returns either the serialized data or errors in JSON format.

    Usage:
        This view is typically mapped to a URL endpoint where clients can
        retrieve weather information in JSON format.
    """
    serializer_class = WeatherSerializer

    def get(self, request):
        """
        Handle GET requests to retrieve weather data.

        Retrieves mock weather data, validates it using `WeatherSerializer`,
        and returns either the serialized data or errors in JSON format.

        Returns:
            Response: JSON response containing weather information or errors.
        """
        try:
            mock_data = get_mock_data()
            serializer = WeatherSerializer(data=mock_data)
            if serializer.is_valid():
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                logger.error(f"Serializer errors: {serializer.errors}")
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"An error occurred while retrieving weather data: {str(e)}")
            return Response(data={"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
