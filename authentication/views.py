from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, get_user_model
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from NGO.models import NgoProfile
from authentication.tokens import account_activation_token
from beneficiaries.forms import SignUpForm
from beneficiaries.models import Beneficiary
from donors.models import Donors
from project_managers.models import ProjectManager

# Create your views here.

User = get_user_model()


def signup_donor(request):
    # sign up a user
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm-password']
        # phone_number = request.POST['phone_number']

        # check if passwords match
        if password == password2:
            # check email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect(request.path_info)
            else:
                # check phone number
                # if User.objects.filter(phone_number=phone_number).exists():
                #     messages.error(request, 'That phone number is being used')
                #     return redirect('signupDonor')
                # else:
                # save the User and redirect them to the log in page with a message to check their inbox for email activation
                user = User.objects.create_user(email=email, password=password, is_donor=True, is_beneficiary=False,
                                                is_ngo=False, is_project_manager=False)
                user.save()

                user.refresh_from_db()
                profile = Donors.objects.filter(user=user).get()
                # profile.first_name = first_name
                # profile.last_name = last_name
                # profile.contact_number = phone_number
                profile.email = email
                profile.save()

                profile.refresh_from_db()
                login(request, user)
                print('user logged in')
                current_site = get_current_site(request)

                subject = 'Activate Your Uwezo Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                send_mail(

                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=settings.FAIL_SILENTLY,

                )

                return redirect('profile_redirect')

        else:
            messages.info(request, 'Your passwords do not match')
            return redirect(request.path_info)
    else:
        return render(request, 'signup_donor.html')


def signup_ngo(request):
    if request.method == 'POST':
        # get the post parameters
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm-password']
        # phone_number = request.POST['phone_number']

        # check if passwords match
        if password == password2:
            # check email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect(request.path_info)
            else:
                # check phone number
                # if User.objects.filter(phone_number=phone_number).exists():
                #     messages.error(request, 'That phone number is being used')
                #     return redirect('signupDonor')
                # else:
                # save the User and redirect them to the log in page with a message to check their inbox for email activation
                user = User.objects.create_user(email=email, password=password, is_donor=False, is_beneficiary=False,
                                                is_ngo=True, is_project_manager=False)
                user.save()

                user.refresh_from_db()
                profile = NgoProfile.objects.filter(user=user).get()
                profile.name = name

                # profile.contact_number = phone_number
                profile.email = email
                profile.save()
                user.refresh_from_db()
                profile.refresh_from_db()
                login(request, user)
                current_site = get_current_site(request)

                subject = 'Activate Your Uwezo Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                send_mail(

                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=settings.FAIL_SILENTLY,

                )

                return redirect('profile_redirect')

        else:
            messages.info(request, 'Your passwords do not match')
            return redirect(request.path_info)
    else:
        return render(request, 'signup_ngo.html')


def signup_beneficiary(request):
    if request.method == 'POST':
        # get the post parameters
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm-password']
        # phone_number = request.POST['phone_number']

        # check if passwords match
        if password == password2:
            # check email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect(request.path_info)
            else:
                # check phone number
                # if User.objects.filter(phone_number=phone_number).exists():
                #     messages.error(request, 'That phone number is being used')
                #     return redirect('signupDonor')
                # else:
                # save the User and redirect them to the log in page with a message to check their inbox for email activation
                user = User.objects.create_user(email=email, password=password, is_donor=False, is_beneficiary=True,
                                                is_ngo=False, is_project_manager=False)
                user.save()

                user.refresh_from_db()
                profile = Beneficiary.objects.filter(user=user).get()

                # profile.contact_number = phone_number
                profile.email = email
                profile.save()

                profile.refresh_from_db()
                current_site = get_current_site(request)

                subject = 'Activate Your Uwezo Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                send_mail(

                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=settings.FAIL_SILENTLY,

                )

                return HttpResponse('signup successfull ')

        else:
            messages.info(request, 'Your passwords do not match')
            return redirect(request.path_info)

    else:
        form = SignUpForm()

        return render(request, 'signup_beneficiary.html', {'form': form})


def signup_pm(request):
    if request.method == 'POST':
        # get the post parameters
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm-password']
        # phone_number = request.POST['phone_number']

        # check if passwords match
        if password == password2:
            # check email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect(request.path_info)
            else:
                # check phone number
                # if User.objects.filter(phone_number=phone_number).exists():
                #     messages.error(request, 'That phone number is being used')
                #     return redirect('signupDonor')
                # else:
                # save the User and redirect them to the log in page with a message to check their inbox for email activation
                user = User.objects.create_user(email=email, password=password, is_donor=False, is_beneficiary=False,
                                                is_ngo=False, is_project_manager=True)
                user.save()

                user.refresh_from_db()
                profile = ProjectManager.objects.filter(user=user).get()
                print('fffffffffffffffffffffffffffff', profile)
                # profile.first_name = first_name
                # profile.last_name = last_name
                # profile.contact_number = phone_number
                profile.email = email
                profile.save()

                profile.refresh_from_db()
                login(request, user)
                current_site = get_current_site(request)

                subject = 'Activate Your Uwezo Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                send_mail(

                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=settings.FAIL_SILENTLY,

                )

                return redirect('profile_redirect')

        else:
            messages.info(request, 'Your passwords do not match')
            return redirect(request.path_info)

    else:
        return render(request, 'signup_pm.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            if Donors.objects.filter(user=request.user).exists():
                # check if user is confirmed
                if Donors.objects.filter(user=request.user).get().email_confirmed == False:
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')
                # elif DoctorProfile.objects.filter(user=request.user).get().is_verified == False:
                #     messages.error(request, 'Your account is not yet approved. Please be patient as we review your application')
                #     return redirect('login')
                else:
                    print('----------------donor')
                    return redirect('/profile')
            elif NgoProfile.objects.filter(user=request.user).exists():
                if NgoProfile.objects.filter(user=request.user).get().email_confirmed == False:
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')
                else:
                    print('----------------ngo')

                    return redirect('/profile')
            elif ProjectManager.objects.filter(user=request.user).exists():
                if ProjectManager.objects.filter(user=request.user).get().email_confirmed == False:
                    print(ProjectManager.objects.filter(user=request.user).get().email_confirmed == False)
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')


                else:
                    return redirect('/profile')
            elif Beneficiary.objects.filter(user=request.user).exists():
                if Beneficiary.objects.filter(user=request.user).get().email_confirmed == False:
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')
                else:

                    return redirect('/profile')

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:

        return render(request, 'login.html')


# create a view to logout users and redirect to home page
def logout_view(request):
    logout(request)
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        user.save()
        if Donors.objects.filter(user=user):
            donor = Donors.objects.filter(user=user).get()
            donor.email_confirmed = True
            donor.save()

            return redirect('login')

        elif NgoProfile.objects.filter(user=user):
            ngo = NgoProfile.objects.filter(user=user).get()
            ngo.email_confirmed = True
            ngo.save()


            print('********************patient yeeeeeeeeeeeeeeey')
            return redirect('login')

        elif ProjectManager.objects.filter(user=user):
            pm = ProjectManager.objects.filter(user=user).get()
            pm.email_confirmed = True
            pm.save()



            return redirect('login')
        elif Beneficiary.objects.filter(user=user):
            beneficiary = Beneficiary.objects.filter(user=user).get()
            beneficiary.email_confirmed = True
            beneficiary.save()

            return redirect('login')
        else:

            return HttpResponse('You are not authorized to view this page')





    else:
        return render(request, 'invalid_activation.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


@login_required
def profile_view(request):
    if request.user.is_authenticated:
        print('----------------user authenticated')

        if Donors.objects.filter(user=request.user):
            # check if the users email is confirmed
            if Donors.objects.filter(user=request.user).get().email_confirmed == False:
                messages.error(request, 'Your account is not yet activated')
                return redirect('login')
            else:
                pk = Donors.objects.filter(user=request.user).get().pk

                return redirect(f'/donor/{pk}')

        elif ProjectManager.objects.filter(user=request.user):
            if ProjectManager.objects.filter(user=request.user).get().email_confirmed == False:
                messages.error(request, 'Your account is not yet activated')
                return redirect('login')
            else:
                pk = ProjectManager.objects.filter(
                    user=request.user).get().pk  # get the primary key of the project manager

                return redirect(f'/updatePm/{pk}')

        elif NgoProfile.objects.filter(user=request.user):
            if NgoProfile.objects.filter(user=request.user).get().email_confirmed == False:
                messages.error(request, 'Your account is not yet activated')
                return redirect('login')
            else:
                ngo = NgoProfile.objects.filter(user=request.user).get()
                pk = ngo.pk

                return redirect(f'/ngo/update/{pk}')

        elif Beneficiary.objects.filter(user=request.user):
            if Beneficiary.objects.filter(user=request.user).get().email_confirmed == False:
                messages.error(request, 'Your account is not yet activated')
                return redirect('login')
            else:
                pk = Beneficiary.objects.filter(user=request.user).get().pk

                return redirect(f'beneficiary/update/{pk}')


        else:
            return HttpResponse('You are not authorized to view this page')


    else:
        return HttpResponse('You are not authorized to view this page')


def loginRedirect(request):
    if request.method == 'POST':
        try:
            username = request.POST['email']
            password = request.POST['password']
        except KeyError as e:
            print(e)
            return render(request, 'login_redirect.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            if Donors.objects.filter(user=request.user).exists():
                # check if user is confirmed
                if Donors.objects.filter(user=request.user).get().email_confirmed == False:
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')
                # elif DoctorProfile.objects.filter(user=request.user).get().is_verified == False:
                #     messages.error(request, 'Your account is not yet approved. Please be patient as we review your application')
                #     return redirect('login')
                else:
                    print('----------------donor',request.POST)
                    return HttpResponseRedirect(request.POST.get('next','/'))
            elif NgoProfile.objects.filter(user=request.user).exists():
                if NgoProfile.objects.filter(user=request.user).get().email_confirmed == False:
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')
                else:
                    print('----------------ngo')

                    return HttpResponseRedirect(request.POST.get('next'))
            elif ProjectManager.objects.filter(user=request.user).exists():
                if ProjectManager.objects.filter(user=request.user).get().email_confirmed == False:
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')


                else:
                    HttpResponseRedirect(request.POST.get('next','/'))
            elif Beneficiary.objects.filter(user=request.user).exists():
                if Beneficiary.objects.filter(user=request.user).get().email_confirmed == False:
                    messages.error(request, 'Your account is not yet activated')
                    return redirect('login')
                else:

                    HttpResponseRedirect(request.META.HTTP_REFERER)

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:

        return render(request, 'login_redirect.html')
