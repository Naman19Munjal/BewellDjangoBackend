from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from .models import Post,Volunteer,MedicineDonation,PostComment
# Create your views here.

def index(request):
    return render(request,"home/index.html")

def games(request):
    return render(request,"home/game.html")

def findtheball(request):
    return render(request,"home/findtheball.html")

def matchslide(request):
    return render(request,"home/mts.html")

def simon(request):
    return render(request,"home/simon.html")

def involve(request):

    if request.method=='POST' and request.FILES['img']:
        title = request.POST.get('title','')
        story = request.POST.get('story','')
        author = request.user.username
        slug = title.replace(' ','-')
        image = request.FILES['img']
        post = Post(title=title,content=story,author=author,slug=slug,image=image)
        post.save()
    post = Post.objects.all().order_by('id')
    params = {'post':post}
    return render(request,"home/post.html",params)

def sign_up(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')
        
        # Create the user
        newuser = User.objects.create_user(username, email, pass1)
        newuser.first_name= fname
        newuser.last_name= lname
        newuser.save()
        login(request, newuser)
        messages.success(request, " Your Bewell Account has been successfully created")
        messages.success(request, "Successfully Logged In")
        return redirect("/")
    else:
        return HttpResponse("404 - Not found")


def log_in(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")
    return HttpResponse("login")

def log_out(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/")

def cures(request):
    return render(request,'home/cures.html')

def volunteer(request):
    if request.method=="POST":
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        emailid = request.POST.get('emailid','')
        phone_no = request.POST.get('phone_no','')
        address = request.POST.get('address','')
        content = request.POST.get('content','')
        vol = Volunteer(fname=fname,lname=lname,emailid=emailid,phone_no=phone_no,address=address,content=content)
        vol.save()
    return render(request,'home/volunteer.html')

def breathing(request):
    return render(request,'home/breathing.html')

def meditation(request):
    return render(request,'home/meditation.html')

def story(request):
    return render(request,'home/story.html')

def song(request):
    return render(request,'home/song.html')

def yoga(request):
    return render(request,'home/yoga.html')

def donate(request):
    if request.method=="POST":
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        address = request.POST.get('address','')
        med = request.POST.get('med','')
        phone_no = request.POST.get('phone_no','')
        md = request.POST.get('md','')
        ed = request.POST.get('ed','')
        quan = request.POST.get('quan','')
        don = MedicineDonation(fname=fname,lname=lname,address=address,med=med,phone_no=phone_no,md=md,ed=ed,quantity=quan)
        don.save()
    return render(request,'home/donation.html')

# def postComment(request):
    

def postview(request,slug):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(id=postSno)
        comment=PostComment(comment= comment, user=user, post=post)
        comment.save()
        # messages.success(request, "Your comment has been posted successfully")
    post = Post.objects.filter(slug=slug).first()
    comments = PostComment.objects.filter(post=post)
    params = {'post':post,'comments':comments}
    return render(request,'home/postdetail.html',params)

def doctor(request):
    return render(request,'home/doctor.html')