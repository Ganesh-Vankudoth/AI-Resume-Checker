from django.shortcuts import render
from django.http import JsonResponse
from .forms import ResumeUploadForm
from .models import Resume
from .utils import extract_text_from_pdf,analyze_resume

# Basic check view
def display(request):
   return JsonResponse({"message": "Resume app running successfully"})

# Main upload view
def upload_resume(request):
    if request.method == 'POST':
        # request.FILES is where the actual file data lives
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume=form.save()
            file_path=resume.file.path
            extracted_text=extract_text_from_pdf(file_path)
            score,matched,missing=analyze_resume(extracted_text,resume.job_role)
            resume.extracted_text=extracted_text
            resume.score=score
            resume.matched_keywords=", ".join(matched)
            resume.save()
            context={
                "job_role":resume.get_job_role_display(),
                "score":score,
                "matched_keywords":matched,
                "missing_keywords":missing
            }
            return render(request,"resume/result.html",context)
    else:
        # Show an empty form for the GET request
        form = ResumeUploadForm()
    
    # Send the form to our HTML template
    return render(request, 'resume/upload.html', {'form': form})