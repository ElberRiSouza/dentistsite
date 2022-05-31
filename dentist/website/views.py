from django.shortcuts import render
from django.core.mail import send_mail


from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def price(request):
    return render(request, 'price.html', {})


def team(request):
    return render(request, 'team.html', {})


def testimonial(request):
    return render(request, 'testimonial.html', {})


def appointment(request):
    if request.method == "POST":
        appointment_name = request.POST['appointment-name']
        appointment_email = request.POST['appointment-email']
        appointment_date = request.POST['appointment-date']
        appointment_time = request.POST['appointment-time']

        send_mail(
            appointment_email,
            f'New appointment from: {appointment_name} \n' "Date " + appointment_date + "Time " + appointment_time,
            'Appointment',
            ['your_email_here@email.com'],)

        return render(request, 'appointment.html', {
            'appointment_name': appointment_name,
            'appointment_email': appointment_email,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time
        })
    else:
        return render(request, 'appointment.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        subject = request.POST['subject']
        message = request.POST['message']

        # template here: https://htmlcodex.com/demo/?item=1837

        send_mail(
            subject,
            f'Message from: {message_name} \n' + message,
            message_email,
            ['your_email_here@email.com'],)

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})

