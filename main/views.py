from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView,TemplateView
from django.urls import reverse, reverse_lazy
from main.tasks import proces, job
from django.shortcuts import redirect
from django.http import JsonResponse
from celery.result import AsyncResult
from django.contrib.sessions.models import Session

def ajaxProgres(request, taskid):
    print("task id ", taskid)
    # status = see_status.apply_async(args=[taskid])
    status = AsyncResult(taskid)
    print("info", status.info)
    print("statte", status.state)
    progress = {'progress': 100}
    return JsonResponse({
        "state": status.state,
        "info": status.info,

    })

def on_raw_message(body):
    print(body)

class ActionTemplateView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.request.session.get('task_id')
        if task_id:
            print('task id ', task_id)
            context["task_id"] = task_id
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        if action == "ok":
            print("ok1")
            task = proces.apply_async()
            print(task.id)
            request.session['task_id'] = task.id
            return redirect("main:a")
        if action == "run":
            print("run")
            result = job.apply_async()
            return redirect("main:a")
        else:
            return self.get(request, *args, **kwargs)