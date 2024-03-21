from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habits.models import Habit
from habits.pagination import HabitPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListApiView(generics.ListAPIView):
    """ Вывод списка привычек пользователя """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    pagination_class = HabitPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class HabitCreateApiView(generics.CreateAPIView):
    """ Создание привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """ Просмотр информации об одной привычке """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class HabitUpdateApiView(generics.UpdateAPIView):
    """ Изменение привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyApiView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListApiView(generics.ListAPIView):
    """ Вывод списка публичных привычек """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination
