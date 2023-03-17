from django.shortcuts import render,HttpResponse,redirect
from resume.models import Resume,Contact,Proof,User_Profile
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import datetime

# Create your views here.
def home(request):
    messages.success(request,'Welcome to GetResume')

    resume=Resume.objects.all()
    img=False
    if request.user.is_authenticated:
        status=User_Profile.objects.filter(username=request.user)[0]
        bool=(status.status)
        print(bool)
        img=status.img
        print(img)
        if not bool:
            messages.warning(request,'<a href="/profile">Complete Your Profile</a>')



    # print(resume)
    params={'resume':resume,'profile':img}
    return render(request,'home.html',params)


def templateview(request,myid):
    template=Resume.objects.filter(sno=myid)
    print(template)
    params={'template':template[0]}
    return render(request,'templateview.html',params)



def checkout(request,myid):
    global bookingid
    
    if request.method=='POST':
        if request.user.is_authenticated:


            obj=Resume.objects.filter(sno=myid)[0]
            name=request.POST.get('name','')
            email = request.POST.get('email', '') 
            phone=request.POST.get('phone','')
            amount = request.POST.get('amount', '')
            contact=Contact(name=name,email=email,phone=phone,amount=amount,r_details=Resume.objects.filter(sno=myid)[0])
            contact.save()
            bookingid=contact.sno


            
            return render(request,'qrpage.html',{'id':bookingid,'price':obj.price})
        else:
            messages.warning(request,'Login Or SingUp to Checkout')

            return redirect('login')




    




        
    template=Resume.objects.filter(sno=myid)
    params={'template':template[0]}

    return render(request,'checkout.html',params)






def check(request,myid):
    if request.user.is_authenticated:
    
        if request.method=='POST':
            obj=Contact.objects.filter(sno=myid)[0]
            print(obj)
            proof=request.FILES.getlist('img')[0]
            print(proof)
            obj2=Proof(info=obj,img=proof,name=request.user,d_date=datetime.date.today())
            obj2.save()
            messages.success(request,'Your Response submitted to us Successfully')

            return redirect('/')
        else:
            return HttpResponse('Error')
    else:
        return redirect('/')



def handlesignup(request):
    if request.method=='POST':
        # get the post parameter
        username=request.POST.get('username','')
        name=request.POST.get('name','')
        signup_email=request.POST.get('signup_email','')
        
        password=request.POST.get('password','')
        password1=request.POST.get('password1','')
        # print(username,name,signup_email,password,password1)
        if len(name.split())!=2:
            messages.error(request,'Enter your full name')
            return redirect('signup')

        fname=name.split()[0]
        lname=name.split()[1]
        # username should be atleast 10 character long
        if len(username)>10:
            messages.error(request,'username must be under 10 characters')
            return redirect('signup')
        # username should be alphanumeric
        
        if not  username.isalnum():
            messages.error(request,'username should only cantain letters and number')
            return redirect('signup')
        # password should be match with confirm password field
        if password!=password1:
            messages.error(request,'Password does not match')
            return redirect('signup')

        
        myuser=User.objects.create_user(username,signup_email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        obj=User_Profile(username=username)
        obj.save()
        
        
        user=authenticate(username=username, password=password)
        login(request,user)


        messages.success(request,"Your GetResume account successfully created")
        return redirect('profile')


    else:
        return render(request,'signup.html')



def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST.get('username','')
        loginpassword=request.POST.get('password','')
        user=authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            
            messages.success(request,"Successfully Logged in")

            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials, Please Try Again')
            return redirect('/')



        
    else:
        return render(request,'login.html')
    


def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('/')







def bookings(request):
    user=request.user
    print(user)
    obj=Proof.objects.filter(name=user)
    # print(obj[0].info.r_details.title)
    if len(obj)==0:
        return render(request,'notfound.html')

    return render(request,'booking.html',{'obj':obj})



def profile(request):
    if request.method=='POST':
        img=request.FILES.getlist('img')
        if len(img)>=1:
            img=img[0]
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        city=request.POST.get('city','')
        gender=request.POST.get('radiobtn','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        glink=request.POST.get('glink','')
        llink=request.POST.get('llink','')
        clg=request.POST.get('clg','')
        syear=request.POST.get('syear','')
        eyear=request.POST.get('eyear','')
        degree=request.POST.get('degree','')
        stream=request.POST.get('stream','')
        tenthage=request.POST.get('10th','')
        twelthhage=request.POST.get('12th','')
        intro=request.POST.get('intro','')
        skills=request.POST.get('skills','')
        Achievement=request.POST.get('Achievement','')
        project=request.POST.get('project','')
        Experience=request.POST.get('Experience','')
        other_Intrests=request.POST.get('other_Intrests','')
        other=request.POST.get('other','')
        print(img,fname,lname,city,gender,email,phone,glink,llink,clg,syear,eyear,degree,stream,tenthage,twelthhage,intro,skills,Achievement,project,Experience,other_Intrests,other)
        
        if len(fname)<=2 or len(lname)<=2 or len(city)<=2 or len(email)<=2 or len(phone)<10 or len(glink)<2 or len(llink)<2 or len(clg)<2 or len(syear)<2 or len(eyear)<2 or len(degree)<2 or len(stream)<2 or len(tenthage)<2 or len(twelthhage)<2 or len(intro)<2 or  len(skills)<2 or  len(Achievement)<2 or  len(project)<2 or  len(Experience)<2 or  len(other_Intrests)<2:
            messages.warning(request,'Invalid Credentials')
            return redirect('profile')
        if len(img)==0:
            obj, created = User_Profile.objects.update_or_create(
            username=request.user,
            defaults={'fname': fname,'lname':lname,'city':city,'gender':gender,'email':email,'phone':phone,'github_link':glink,'linkedin_link':llink,'college':clg,'s_year':syear,'e_year':eyear,'degree':degree,'stream':stream,'tenth_age':tenthage,'twelth_age':twelthhage,'about':intro,'skills':skills,'achievement':Achievement,'projects':project,'exprience':Experience,'hobbies':other_Intrests,'other':other,'status':True},
            )
        else:
            obj, created = User_Profile.objects.update_or_create(
            username=request.user,
            defaults={'img':img,'fname': fname,'lname':lname,'city':city,'gender':gender,'email':email,'phone':phone,'github_link':glink,'linkedin_link':llink,'college':clg,'s_year':syear,'e_year':eyear,'degree':degree,'stream':stream,'tenth_age':tenthage,'twelth_age':twelthhage,'about':intro,'skills':skills,'achievement':Achievement,'projects':project,'exprience':Experience,'hobbies':other_Intrests,'other':other,'status':True},
            )



        messages.success(request,'Profile Updated Successfully')
        
        return redirect('profile')
    

    info=User_Profile.objects.filter(username=request.user)[0]
    return render(request,'info.html',{'info':info})