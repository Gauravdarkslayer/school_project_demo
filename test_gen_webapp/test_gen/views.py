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
    print("this works")
    questionnaire={}
    fill_blanks = {}
    i=1
    number_of_iterations = 0
    for content in doc.paragraphs:
        if ("Q"+str(i) or "QUESTION"+str(i)) in content.text.upper():
            print(content.text)
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
        elif ('fill in the blanks') in content.text.lower():
            print("I am inside Fill in the Blanks")
            fill_blanks[content.text] = []
            next_index = number_of_iterations+1
            
            for i in range(next_index, len(doc.paragraphs)):
                if "_" in doc.paragraphs[i].text:
                    fill_blanks[content.text].append(doc.paragraphs[i].text)
                elif " " == doc.paragraphs[i].text:
                    continue
                else:
                    break

            print("Data of Fill in the blanks is ", fill_blanks)
        number_of_iterations += 1
    print(questionnaire)

    return render(request,"show_questions.html",{'context':questionnaire, 'fill_blanks':fill_blanks})
