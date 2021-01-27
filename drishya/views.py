from django.shortcuts import render,redirect
from drishya.models import images2,addimages,Profile,Adddata,Payment
from drishya.forms import picture,reg
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import UserRegisterForm, ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
import re
# from bank_account_validator.core import Bank
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
# Create your views here.
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if name == "" or email == "" or subject == "" or message == "":
            messages.info(request,'Please Fill All The Details')
            return redirect('/')
        elif (isValid(int(subject)) == False):
            messages.info(request,'Please enter a valid mobile number')
            return redirect('/')
        elif (check(email) == False):
            messages.info(request,'Please enter a valid Email')
            return redirect('/')
        else:
            res = send_mail(subject,name + " - " + email + " - " + message,email,[EMAIL_HOST_USER],fail_silently=False)
            messages.info(request,'Email Sent')
    else:
        return render(request,"index.html")

def login(request):
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                current_user = request.user
                new=current_user.id-14
                print(new)
                dests=Profile.objects.get(id=new)
                return HttpResponseRedirect("allposts",)
            else:
                messages.info(request,'Please Enter Correct Email And Password')
                return redirect('/login/')
    else:
        dests=addimages.objects.get(id=1)
        images=addimages.objects.get(id=2)  
        hey = addimages.objects.get(id=5)
        context = {
            'dests':dests,
            'images':images,
            'hey':hey
        }

        return render(request,'login.html', context)

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        mobile_no=request.POST['mobile_no']
        s = str(mobile_no)
        if username == "" or email == "" or password1 == "" or password2 == "" or mobile_no == "" :
                messages.info(request,'Please fill all the details')
                return redirect('drishya:register')
        else:
            if password1==password2:    
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username Is Already Taken')
                    return redirect('drishya:register')
                elif (isValid(s) == False):
                    messages.info(request,'Please enter a valid mobile number')
                    return redirect('drishya:register')
                elif (check(email) == False):
                    messages.info(request,'Please enter a valid Email')
                    return redirect('drishya:register')
                elif (password_check(password1) == False):
                    messages.info(request,'Please enter the password as per the details given')
                    return redirect('drishya:register')
                else:
                    img=request.FILES['img']
                    user=User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    hey=Profile.objects.create(mobile_no=mobile_no,img=img,wallet = 0)
                    hey.save()
                    return HttpResponseRedirect("/login/")
            else:
                messages.info(request,'Please enter the same password in confirm password')
                return redirect('drishya:register')
    else:
        form = UserRegisterForm()
        profile_form = ProfileUpdateForm()
        dests=addimages.objects.get(id=1)
        images=addimages.objects.get(id=2)
        hey = addimages.objects.get(id = 5)
        return render(request,"register.html",{'dests':dests,'images':images,'form':form,'profile_form':profile_form,'hey':hey})
def allposts(request):
    heyy=images2.objects.all()
    dests=heyy.order_by("id")
    current_user = request.user
    new=current_user.id-14
    prof=Profile.objects.get(id=new)
    name = current_user.username
    new1 = Adddata.objects.filter(name=name)
    hey = addimages.objects.get(id = 5)
    return render(request,"allposts.html",{'dests':dests,'prof':prof,'new1':new1,'hey':hey})
def addposts(request):
    if request.method == 'POST':
        current_user = request.user
        name=current_user.username
        new=current_user.id-14
        hey = Profile.objects.get(id = new)
        mobile_no = hey.mobile_no
        profile_pic = hey.img
        form=picture(request.POST,request.FILES)
        #if form.is_valid():
        imaa=request.FILES['img']
        caption=request.POST['caption']
        price=request.POST['price']
        u=images2.objects.create(img=imaa,caption=caption,price=price,name=name,mobile_no = mobile_no,likes = 0,profile_pic=profile_pic)
        u.save()
        return HttpResponseRedirect("allposts")
        #else:
         #   form.errors()
    else:
        current_user = request.user
        new=current_user.id-14
        prof=Profile.objects.get(id=new)
        form=picture()
        return render(request,"addpost.html",context = {'form':form,'prof':prof})
def myposts(request,pk):
    hi=images2.objects.get(id=pk)
    myname=hi.name
    haaa=images2.objects.filter(name=myname)
    dests=haaa.order_by("id")
    current_user = request.user
    new=current_user.id-14
    prof=Profile.objects.get(id=new)
    name = current_user.username
    new1 = Adddata.objects.filter(name=name)
    hey = addimages.objects.get(id = 5)
    return render(request,"myposts.html",{'dests':dests,'prof':prof,'new1':new1,'hey':hey})
def payment(request,pk): 
    if request.method=='POST':
        dests=images2.objects.get(id=pk)
        card_no = request.POST['card_no']
        card_name = request.POST['card_name']
        amount = dests.price
        month = request.POST['month']
        year = request.POST['year']
        cvv = request.POST['cvv']
        if card_no == "" or card_name == "" or month == "" or year == "" or cvv == "": 
            messages.info(request,'Please Fill All The Details')
            return HttpResponseRedirect("payment")
        else:
            if validate(card_no) == False:
                messages.info(request,'Enter Valid Card Number')
                return HttpResponseRedirect("payment")
            elif dateValidate(month) == False:
                messages.info(request,'Enter Valid Expiry Date')
                return HttpResponseRedirect("payment")
            elif dateValidate(year) == False:
                messages.info(request,'Enter Valid Expiry Date')
                return HttpResponseRedirect("payment")
            elif CvvValidate(cvv) == False:
                messages.info(request,'Enter Valid CVV number')
                return HttpResponseRedirect("payment")
            else:
                
                dests = images2.objects.get(id = pk)
                hey = dests.name
                price = dests.price
                hi = User.objects.get(username = hey)
                mee = hi.id - 14
                ho = Profile.objects.get(id = mee)
                current_user = request.user
                new  = current_user.id - 14
                now = Profile.objects.get(id = new)
                if now.wallet < dests.price:
                    messages.info(request,'Your Wallet has less amount than the image price')
                    return HttpResponseRedirect("payment")
                else:
                    dests.purchased="Purchased"
                    dests.save()
                    now.wallet = now.wallet - price
                    now.save()
                    ho.wallet = ho.wallet + price
                    ho.save()
                    usr = Payment.objects.create(card_no = card_no,card_name = card_name,amount = amount)
                    usr.save()
                    return HttpResponseRedirect("afterpayment")
    else:
        image1=addimages.objects.get(id=3)
        image2=addimages.objects.get(id=4)
        current_user = request.user
        new=current_user.id-14
        prof=Profile.objects.get(id=new)
        dests = images2.objects.get(id = pk)
        hey = addimages.objects.get(id = 5)
        return render(request,"payment.html",{'image1':image1,'image2':image2,'prof':prof,'dests':dests,'hey':hey})
def afterpayment(request,pk):
    dests=images2.objects.get(id=pk)
    current_user = request.user
    new=current_user.id-14
    prof=Profile.objects.get(id=new)
    return render(request,"afterpayment.html",{'dests':dests,'prof':prof})
def like(request):
        liked=request.POST['liked']
        dests=images2.objects.get(id=liked)
        dests.likes=dests.likes + 1
        dests.save()
        current_user = request.user
        name=current_user.username
        img_id = liked
        new1 = Adddata.objects.create(name=name,img_id=img_id)
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
def mine(request):
    current_user = request.user
    new=current_user.id-14
    prof=Profile.objects.get(id=new)
    myname=request.user.username   
    haa=images2.objects.filter(name=myname)
    dests = haa.order_by("id")
    name = current_user.username
    new1 = Adddata.objects.filter(name=name)
    hey = addimages.objects.get(id = 5)
    return render(request,"mine.html",{'dests':dests,'prof':prof,'hey':hey,'new1':new1}) 
def newallposts(request,pk):
    return redirect("drishya:allposts")
def dislike(request):
        disliked=request.POST['disliked']
        dests=images2.objects.get(id=disliked)
        dests.likes=dests.likes - 1
        dests.save()
        current_user = request.user
        name=current_user.username
        img_id = disliked
        new1 = Adddata.objects.get(name=name,img_id=img_id).delete()
def addwallet(request):
    if request.method=='POST':
        card_no = request.POST['card_no']
        card_name = request.POST['card_name']
        month = request.POST['month']
        year = request.POST['year']
        cvv = request.POST['cvv']
        amount = request.POST['amount']
        if card_no == "" or card_name == "" or month == "" or year == "" or cvv == "" or amount == "": 
            messages.info(request,'Please Fill All The Details')
            return HttpResponseRedirect("addwallet")
        else:
            if validate(card_no) == False:
                messages.info(request,'Enter Valid Card Number')
                return HttpResponseRedirect("addwallet")
            elif dateValidate(month) == False:
                messages.info(request,'Enter Valid Expiry Date')
                return HttpResponseRedirect("addwallet")
            elif dateValidate(year) == False:
                messages.info(request,'Enter Valid Expiry Date')
                return HttpResponseRedirect("addwallet")
            elif CvvValidate(cvv) == False:
                messages.info(request,'Enter Valid CVV number')
                return HttpResponseRedirect("addwallet")
            else:
                current_user = request.user
                new = current_user.id - 14
                hey = Profile.objects.get(id = new)
                hey.wallet = hey.wallet + int(amount)
                hey.save()
                usr = Payment.objects.create(card_no = card_no,card_name = card_name,amount = amount)
                usr.save()
                return HttpResponseRedirect("allposts")

    else:
        image1=addimages.objects.get(id=3)
        image2=addimages.objects.get(id=4)
        current_user = request.user
        new=current_user.id-14
        prof=Profile.objects.get(id=new)
        hey = addimages.objects.get(id = 5)
        return render(request,"addwallet.html",{'image1':image1,'image2':image2,'prof':prof,'hey':hey})
def getwallet(request):
    if request.method=='POST':
        bank_name = request.POST['bank_name']
        acc_no = request.POST['acc_no']
        ifsc_code = request.POST['ifsc_code']
        if acc_no == "" or bank_name == "" or ifsc_code == "": 
            messages.info(request,'Please Fill All The Details')
            return HttpResponseRedirect("getwallet")
        else:
            if IFSCValidate(ifsc_code) == False:
                messages.info(request,'Please enter the correct IFSC Code')
                return HttpResponseRedirect("getwallet")
            else:
                current_user = request.user
                new = current_user.id - 14
                hey = Profile.objects.get(id = new)
                hey.wallet = 0
                hey.save()
                return HttpResponseRedirect("allposts")
    else:
        image1=addimages.objects.get(id=8)
        image2=addimages.objects.get(id=4)
        current_user = request.user
        new=current_user.id-14
        prof=Profile.objects.get(id=new)
        hey = addimages.objects.get(id = 5)
        return render(request,"getwallet.html",{'image1':image1,'image2':image2,'prof':prof,'hey':hey})
def newaddwallet(request,pk):
    return redirect("drishya:addwallet")
def newgetwallet(request,pk):
    return redirect("drishya:getwallet")
def newlogout(request,pk):
    return redirect("drisya:logout")
def isValid(s): 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    if Pattern.match(s):
        return True
    else:
        return False
def check(email):  
    if(re.search(regex,email)):  
        return True  
          
    else:  
        return False
def password_check(password1): 
      
    SpecialSym =['$', '@', '#', '%','&','*'] 
      
    if len(password1) < 6: 
        return False        
    elif not any(char.isdigit() for char in password1): 
        return False
          
    elif not any(char.isupper() for char in password1): 
        return False
          
    elif not any(char.islower() for char in password1): 
        return False
          
    elif not any(char in SpecialSym for char in password1): 
        return False
    else:
        return True
def validate(card_no):
    card_no = str(card_no)
    re.sub(r' ', '', card_no)
    count = 0
    for i in range(len(card_no)):
        val = int(card_no[-(i+1)])
        if i % 2 == 0:
            count += val
        else:
            count += int(str(2 * val)[0])
            if val > 5:
                count += int(str(2 * val)[1])
    if count % 10 == 0:
        return True
    else:
        return False
def dateValidate(s):
    if len(s) != 2: 
        return False        
    else:
        return True
def CvvValidate(s):
    if len(s) != 3: 
        return False        
    else:
        return True
def IFSCValidate(s):
    if len(s) !=11: 
        return False        
    else:
        return True