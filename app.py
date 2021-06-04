from flask import Flask, render_template, redirect, url_for, session,request
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField,RadioField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class ProjectForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    mobile=StringField('Mobile Number', validators=[DataRequired()])
    email=StringField('Email ID',validators=[DataRequired(),Email()])
    title=StringField('Project Title',validators=[DataRequired()])
    description=StringField('Project Description',validators=[DataRequired()])
    submit1=SubmitField('Submit Request')

class WorkshopForm(FlaskForm):
    name2=StringField('Name',validators=[DataRequired()])
    organisation=StringField('Organisation',validators=[DataRequired()])
    mobile2=StringField('Mobile Number',validators=[DataRequired()])
    email2=StringField('Email ID',validators=[DataRequired(),Email()])
    workshop=RadioField('Workshops',choices=[('Drone Programming','Drone Programming'),('RC Plane Design','RC Plane Design'),('Structural and Flow Analysis of RC Planes','Structural and Flow Analysis of RC Planes'),('Material Selection for RC Planes','Maaterial Selection')])
    attendees=StringField('Expected Number of Attendees',validators=[DataRequired()])
    submit2=SubmitField('Submit Request')

class ContactForm(FlaskForm):
    name3=StringField('Name',validators=[DataRequired()])
    mobile3=StringField('Mobile Number', validators=[DataRequired()])
    email3=StringField('Email ID',validators=[DataRequired(),Email()])
    message=StringField('Type your message here',validators=[DataRequired()])
    submit3=SubmitField('Submit')

app=Flask(__name__)

app.config['SECRET_KEY']='mykey'
app.config['DEBUG']=True
app.config['TESTING']=False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='teamaviatorsforms@gmail.com'
app.config['MAIL_PASSWORD']='ljmbnoiplxwgpexz'
app.config['MAIL_DEFAULT_SENDER']='teamaviatorsforms@gmail.com'
app.config['MAIL_MAX_MAILS']=None
app.config['MAIL_ASCII_ATTACHMENTS']=False


mail=Mail(app)

#configure the functions for mailing

def project_mail(name,mobile,email,title,description):
    global mail
    msg1=Message('Project Request Received',recipients=[email])
    msg1.body='Dear '+name+',\n\nYour project request has been received by Team Aviators International. We will review your request and get back to you soon.\n\nRegards,\nTeam Aviators International'
    mail.send(msg1)
    msg2=Message('New Project Request',recipients=['teamaviatorsinternational@gmail.com'])
    msg2.body='Name of Applicant: {}\n\nMobile Number: {}\n\nEmail ID: {}\n\nProject Title: {}\n\nProject Description: {}'.format(name,mobile,email,title,description)
    mail.send(msg2)

def contact_mail(name,mobile,email,message):
    global mail
    msg1=Message('Contact Enquiry Received',recipients=[email])
    msg1.body='Dear '+name+',\n\nThank you for reaching out to us. Somebody from our team will soon contact you to further know your interests and queries.\n\nRegards,\nTeam Aviators International'
    mail.send(msg1)
    msg2=Message('New Contact Enquiry',recipients=['teamaviatorsinternational@gmail.com'])
    msg2.body='Name of Applicant: {}\n\nMobile Number: {}\n\nEmail ID: {}\n\nMessage: {}'.format(name,mobile,email,message)
    mail.send(msg2)

def workshop_mail(name,organisation,mobile,email,workshop,attendees):
    global mail
    msg1=Message('Workshop Request Received',recipients=[email])
    msg1.body='Dear '+name+',\n\nYour request for a workshop on '+workshop+ ' has been received successfully by Team Aviators International. We will contact you soon for further proceedings.\n\nRegards,\nTeam Aviators International'
    mail.send(msg1)
    msg2=Message('New Workshop Request',recipients=['teamaviatorsinternational@gmail.com'])
    msg2.body='Name of Applicant: {}\n\nOrganisation: {}\n\nMobile Number: {}\n\nEmail ID: {}\n\nWorkshop: {}\n\nExpected Number of Attendees: {}'.format(name,organisation,mobile,email,workshop,attendees)
    mail.send(msg2)

@app.route('/',methods=['GET','POST'])
def index():
    form1=ProjectForm()
    form2=WorkshopForm()
    form3=ContactForm()

    if(form1.submit1.data and form1.validate()):
        session['name']=form1.name.data
        session['mobile']=form1.mobile.data
        session['email']=form1.email.data 
        session['title']=form1.title.data
        session['description']=form1.description.data
        project_mail(session['name'],session['mobile'],session['email'],session['title'],session['description'])
        return redirect(url_for('index'))
    
    if(form2.submit2.data and form2.validate()):
        session['name2']=form2.name2.data
        session['organisation']=form2.organisation.data
        session['mobile2']=form2.mobile2.data
        session['email2']=form2.email2.data
        session['workshop']=form2.workshop.data
        session['attendees']=form2.attendees.data
        workshop_mail(session['name2'],session['organisation'],session['mobile2'],session['email2'],session['workshop'],session['attendees'])
        return redirect(url_for('index'))
    
    if(form3.submit3.data and form3.validate()):
        session['name3']=form3.name3.data
        session['mobile3']=form3.mobile3.data
        session['email3']=form3.email3.data
        session['message']=form3.message.data
        contact_mail(session['name3'],session['mobile3'],session['email3'],session['message'])
        return redirect(url_for('index'))


    return render_template("homepage.html",form1=form1, form2=form2, form3=form3)


@app.route('/about_us',methods=['GET','POST'])
def about_us():
    form1=ProjectForm()
    form2=WorkshopForm()
    form3=ContactForm()

    if(form1.submit1.data and form1.validate()):
        session['name']=form1.name.data
        session['mobile']=form1.mobile.data
        session['email']=form1.email.data 
        session['title']=form1.title.data
        session['description']=form1.description.data
        project_mail(session['name'],session['mobile'],session['email'],session['title'],session['description'])
        return redirect(url_for('about_us'))
    
    if(form2.submit2.data and form2.validate()):
        session['name2']=form2.name2.data
        session['organisation']=form2.organisation.data
        session['mobile2']=form2.mobile2.data
        session['email2']=form2.email2.data
        session['workshop']=form2.workshop.data
        session['attendees']=form2.attendees.data
        workshop_mail(session['name2'],session['organisation'],session['mobile2'],session['email2'],session['workshop'],session['attendees'])
        return redirect(url_for('about_us'))
    
    if(form3.submit3.data and form3.validate()):
        session['name3']=form3.name3.data
        session['mobile3']=form3.mobile3.data
        session['email3']=form3.email3.data
        session['message']=form3.message.data
        contact_mail(session['name3'],session['mobile3'],session['email3'],session['message'])
        return redirect(url_for('about_us'))
    return render_template("team.html",form1=form1, form2=form2, form3=form3)

@app.route('/gallery',methods=['GET','POST'])
def gallery():
    form1=ProjectForm()
    form2=WorkshopForm()
    form3=ContactForm()

    if(form1.submit1.data and form1.validate()):
        session['name']=form1.name.data
        session['mobile']=form1.mobile.data
        session['email']=form1.email.data 
        session['title']=form1.title.data
        session['description']=form1.description.data
        project_mail(session['name'],session['mobile'],session['email'],session['title'],session['description'])
        return redirect(url_for('gallery'))
    
    if(form2.submit2.data and form2.validate()):
        session['name2']=form2.name2.data
        session['organisation']=form2.organisation.data
        session['mobile2']=form2.mobile2.data
        session['email2']=form2.email2.data
        session['workshop']=form2.workshop.data
        session['attendees']=form2.attendees.data
        workshop_mail(session['name2'],session['organisation'],session['mobile2'],session['email2'],session['workshop'],session['attendees'])
        return redirect(url_for('gallery'))
    
    if(form3.submit3.data and form3.validate()):
        session['name3']=form3.name3.data
        session['mobile3']=form3.mobile3.data
        session['email3']=form3.email3.data
        session['message']=form3.message.data
        contact_mail(session['name3'],session['mobile3'],session['email3'],session['message'])
        return redirect(url_for('gallery'))
    return render_template("gallery.html",form1=form1, form2=form2, form3=form3)

@app.route('/projects',methods=['GET','POST'])
def projects():
    form1=ProjectForm()
    form2=WorkshopForm()
    form3=ContactForm()

    if(form1.submit1.data and form1.validate()):
        session['name']=form1.name.data
        session['mobile']=form1.mobile.data
        session['email']=form1.email.data 
        session['title']=form1.title.data
        session['description']=form1.description.data
        project_mail(session['name'],session['mobile'],session['email'],session['title'],session['description'])
        return redirect(url_for('projects'))
    
    if(form2.submit2.data and form2.validate()):
        session['name2']=form2.name2.data
        session['organisation']=form2.organisation.data
        session['mobile2']=form2.mobile2.data
        session['email2']=form2.email2.data
        session['workshop']=form2.workshop.data
        session['attendees']=form2.attendees.data
        workshop_mail(session['name2'],session['organisation'],session['mobile2'],session['email2'],session['workshop'],session['attendees'])
        return redirect(url_for('projects'))
    
    if(form3.submit3.data and form3.validate()):
        session['name3']=form3.name3.data
        session['mobile3']=form3.mobile3.data
        session['email3']=form3.email3.data
        session['message']=form3.message.data
        contact_mail(session['name3'],session['mobile3'],session['email3'],session['message'])
        return redirect(url_for('projects'))
    return render_template("projects.html",form1=form1, form2=form2, form3=form3)


if __name__=='__main__':
    app.run()
