from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact, Donate
from store.models import PlayStore
from .paytm import Checksum

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']

        if len(name) < 2 or len(email) < 2 or len(phone) < 10 or len(phone) > 13 or len(description) < 2:
            messages.error(request, "Submit again with relevant information")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, description=description)
            contact.save()
            messages.success(
                request, "Thank you for your response, I'll respond ASAP!")

    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    searchQuery = request.GET['query']

    if len(searchQuery) > 71:
        searchResult = PlayStore.objects.none()
    else:
        searchResultTitle = PlayStore.objects.filter(
            title__icontains=searchQuery)
        searchResultDescription = PlayStore.objects.filter(
            description__icontains=searchQuery)
        searchResult = searchResultTitle.union(searchResultDescription)

    if searchResult.count() == 0:
        messages.warning(request, "Sorry, I can't serve for : " + searchQuery)

    results = {"searchResult": searchResult, 'searchQuery': searchQuery}
    return render(request, 'home/search.html', results)


def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['first']
        lastName = request.POST['last']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm']

        if len(username) < 2 or len(username) > 10:
            messages.error(
                request, "Your username must be 2 to 10 characters long")
            return redirect("/")
        if password != confirmPassword:
            messages.error(request, "Password didn't match")
            return redirect("/")
        if password.length() < 8:
            messages.error(
                request, "Password must be at least 8 characters long")
            return redirect("/")
        if len(firstName) < 2 or len(lastName) < 2:
            messages.error(
                request, "Your name and last name cannot be less than two characters")
            return redirect("/")
        if username.isdigit():
            messages.error(request, "Username must have an alphabet")
            return redirect("/")
        if firstName.isdigit():
            messages.error(request, "Name cannot be numerical")
            return redirect("/")
        if lastName.isdigit():
            messages.error(request, "Name cannot be numerical")
            return redirect("/")

        user = User.objects.create_user(username, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()

        messages.success(
            request, "Congratulations, You have successfully joined DevOM!")

        return redirect('/')
    else:
        return render(request, '404NotFound.html')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome " + str(request.user) +
                             ", You're successfully logged in")
            return redirect("/")
        else:
            messages.error(
                request, "I coundn't identify you, please try again.")
            return redirect("/")
    return render(request, '404NotFound.html')


def userLogout(request):
    user = str(request.user)
    logout(request)
    messages.success(
        request, "You are successfully logged out, see you soon, " + user + "!")
    return redirect("/")


def donate(request):
    if request.method == 'POST':
        firstName = request.POST['first-name']
        lastName = request.POST['last-name']
        email = request.POST['email']
        amount = request.POST['amount']
        description = request.POST.get('description', '')

        if len(firstName) < 2 or len(lastName) < 2:
            messages.error(
                request, "Your first name and last name cannot be less than two characters")
            return render(request, "home/donate.html")
        if len(amount) < 2 or int(amount) == 0:
            messages.error(request, "Payment amount cannot be 0")
            return render(request, "home/donate.html")

        donate = Donate(description=description,
                        first_name=firstName, last_name=lastName, email=email, amount=amount)
        donate.save()

        id = donate.sno
        MERCHANT_KEY = 'Q3Tz5XNdK6hC4J6S'

        param_dict = {
            'MID': 'VMjwTa47205061452223',
            'ORDER_ID': str(id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/donateHandler',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
            param_dict, MERCHANT_KEY)

        return render(request, 'home/paytm.html', {'param_dict': param_dict})

    return render(request, "home/donate.html")


@csrf_exempt
def donateHandler(request):
    MERCHANT_KEY = 'Q3Tz5XNdK6hC4J6S'

    form = request.POST

    response_dict = {}

    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            messages.success(
                request, "Thank you for your donation!\nYour donation of " + str(response_dict['CURRENCY']) + " " + str(response_dict['TXNAMOUNT']) + " is successful at " + str(response_dict['TXNDATE']))
        else:
            messages.error(request, "Donation failed")
    return redirect("/donate")


def errorHandler(request, slug):
    return render(request, "404NotFound.html")
