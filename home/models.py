from django.db import models
import uuid
import random as rd
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Question(BaseModel):
    category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        data = []
        rd.shuffle(answer_objs)
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct': answer_obj.is_correct,
            })
        return data

class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

