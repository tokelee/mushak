from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import User


def index(request):
    description = "Discover a new level of web development and programming with Mushak Tech Ventures professional courses. Our project-based approach provides hands-on experience to solidify complex concepts, with explanations delivered in an easy-to-understand manner"
    title = "Mushak Tech Ventures Programming training"
    response = render(request, 'tutorial/index.html',
                      {'description': description, 'title': title})
    return response


def apply(request):
    description = "Discover a new level of web development and programming with Mushak Tech Ventures professional courses. Our project-based approach provides hands-on experience to solidify complex concepts, with explanations delivered in an easy-to-understand manner"
    title = "Mushak Tech Ventures Programming training application form"
    if request.method == 'POST':
        course_of_interest = request.POST['course']
        name = request.POST['fullname']
        email = request.POST['email']
        gender = request.POST['gender']
        date_of_birth = request.POST['dob']
        address = request.POST['address']
        phone_number = request.POST['phone']
        educational_background = request.POST['education']
        occupation = request.POST['occupation']
        learning_mode = request.POST['learning_mode']
        sponsorship = request.POST['sponsor']
        sponsor_relationship = request.POST['sponsor_relationship']
        sponsor_phone_number = request.POST['sponsor_phone']
        how_did_you_hear_about_us = request.POST['how_did_you_hear_about_us']
        user_new_record = User(course_of_interest=course_of_interest, name=name, email=email, gender=gender, date_of_birth=date_of_birth, address=address, phone_number=phone_number, educational_background=educational_background,
                               occupation=occupation, learning_mode=learning_mode, sponsorship=sponsorship, sponsor_relationship=sponsor_relationship, sponsor_phone_number=sponsor_phone_number, how_did_you_hear_about_us=how_did_you_hear_about_us)
        user_new_record.save()
        return HttpResponseRedirect('/thank-you')
    else:
        response = render(request, 'tutorial/apply.html',
                          {'description': description, 'title': title})
        return response


def thank_you(request):
    description = "Thank you for applying to a new level of web development and programming with Mushak Tech Ventures professional courses. Our project-based approach provides hands-on experience to solidify complex concepts, with explanations delivered in an easy-to-understand manner"
    title = "Thank you for applying to a new level of web development and programming with Mushak Tech Ventures professional courses."
    response = render(request, 'tutorial/thank_you.html',
                      {'description': description, 'title': title})
    return response


def frontend(request):
    description = "Discover a new level of web development and programming with Mushak Tech Ventures professional courses. Our project-based approach provides hands-on experience to solidify complex concepts, with explanations delivered in an easy-to-understand manner"
    title = "Mushak Tech Ventures Frontend web development"
    response = render(request, 'tutorial/frontend.html',
                      {'description': description, 'title': title})
    return response


def backend(request):
    description = "Discover a new level of web development and programming with Mushak Tech Ventures professional courses. Our project-based approach provides hands-on experience to solidify complex concepts, with explanations delivered in an easy-to-understand manner"
    title = "Mushak Tech Ventures Frontend web development"
    response = render(request, 'tutorial/frontend.html',
                      {'description': description, 'title': title})
    return response
