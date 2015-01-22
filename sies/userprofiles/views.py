from django.shortcuts import render  
from .forms import UserForm, UserProfileForm, LoginForm
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.forms import User
from userprofiles.models import UserProfile

# Create your views here.
def register(request):

	registered = False 

	if request.method == 'POST':
		user_form = UserForm(request.POST or None)
		profile_form = UserProfileForm(request.POST or None)
		username = request.POST.get('username')
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			#una vez hasheado, actualizamos el objeto user
			user.save()
			 # Now sort out the UserProfile instance.
	         # Since we need to set the user attribute ourselves, we set commit=False.
	         # This delays saving the model until we're ready to avoid integrity problems.
	        profile = profile_form.save(commit=False)
	        
	        profile.username = username

	        profile.save()

	        registered = True
	    #else:
	    	#print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'registro.html', {'user_form': user_form, 'profile_form': profile_form ,'registered': registered })

def login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
			# Redirect to a success page.
			#else:
			# Return 
		#else:
			# Return 
	return render(request, 'signin.html', {'form':form})


def userprofile(request):

	registered = False

	if request.method == 'POST':
		profile_form = UserProfileForm(request.POST or None)
		if profile_form.is_valid():
			userprof = profile_form.save()
			registered = True
	else:
		profile_form = UserProfileForm()

	title = "UserProfile"

	return render(request, 'userprofile.html', {'profile_form': profile_form, 'title': title})
