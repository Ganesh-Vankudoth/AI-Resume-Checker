from django.shortcuts import render
from django.http import JsonResponse
from .forms import ResumeUploadForm
from .models import Resume

# Basic check view
def display(request):
   return JsonResponse({"message": "Resume app running successfully"})

# Main upload view
def upload_resume(request):
    if request.method == 'POST':
        # request.FILES is where the actual file data lives
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": "success", 
                "message": "Resume uploaded and saved to media/resumes/ folder!"
            })
    else:
        # Show an empty form for the GET request
        form = ResumeUploadForm()
    
    # Send the form to our HTML template
    return render(request, 'resume/upload.html', {'form': form})