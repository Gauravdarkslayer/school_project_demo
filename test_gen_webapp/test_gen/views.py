from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_doc_upload_page(request):
    return render(request,'doc_upload.html')


def doc_processing(request):
    file = request.FILES["mydocument"]
    # print(request.FILES)
    print("this is file object",file)
    # current_user_email = request.session["email"]
    import docx
    try:
        doc = docx.Document('file.docx')
        print("success")
    except Exception as e:
        print(e)
    
    doc = docx.Document(file)
    print("this workds")
    questionnaire={}
    i=1

    for content in doc.paragraphs:
        if ("Q"+str(i) or "QUESTION"+str(i)) in content.text.upper():
            
            # questionnaire["question"+str(i)] = content.text
            questionnaire[content.text] =[]
            i=i+1
            j=1
            for option in doc.paragraphs:
                # print("this is option",option.text.upper())
                if "OPTION"+" "+str(j) in option.text.upper():
                    print("check")
                    questionnaire[content.text].append(option.text)
                    j= j+1
                if "ANSWER" in option.text.upper():
                    print("get answer")
                    questionnaire[content.text].append(option.text)
                    break        
    print(questionnaire)

    return render(request,"show_questions.html",{'context':questionnaire})
