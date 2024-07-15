from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, 'base.html')

def home(request):
    cards = [
            {
                "category": "Lakhs",
                "img_src": 'images/lakh1.jpg',
                "title": "M3M Broadway",
                "description": " Sector 71, Gurugram ",
                "description1": "Retail, F&B, Office Space, Gaming Zone , Service Apartment",
                "price": "50 Lakhs* Onwards"
            },
            {
                "category": "Crore",
                "img_src": 'images/crore1.jpg',
                "title": "M3M 65th Avenue",
                "description": "Sector 65, Gurugram ",
                "description1": "Retails, Food Court, Multiplex, F&B , Studio Apts.",
                "price": "1 Cr* Onwards"
            },
            {
                "category": "Lakhs",
                "img_src": 'images/lakh2.jpg',
                "title": "M3M CapitalWalk",
                "description": "Sector 113,Gurugram ",
                "description1": "Retails, Food Court, Anchor Units",
                "price": "75 Lakhs* Onwards"
            },
            {
                "category": "Lakhs",
                "img_src": 'images/lakh3.jpg',
                "title": "M3M Route 65",
                "description": "Sector 65, Gurugram ",
                 "description1": "High-Street, Retail Market",
                "price": " 88 Lakhs* Onwards"
            },
            {
                "category": "Lakhs",
                "img_src": 'images/lakh4.jpg',
                "title": "M3M Atrium 57",
                "description": "Sector 57, Gurugram ",
                 "description1": "Retail Shops, F & B",
                "price": "87 Lakhs* Onwards"
            },
            {
                "category": "Crore",
                "img_src": 'images/crore2.jpg',
                "title": "M3M Jewel",
                "description": "Sector 25, Gurugram ",
                 "description1": "Luxury retail, fine dinning, multiplex",
                "price": " 500 Sq. Ft.* Onwards"
            },
            {
                "category": "Lakhs",
                "img_src": 'images/lakh5.jpg',
                "title": "M3M Corner Walk",
                "description": "Sector 74, Gurugram",
                 "description1": "Retail Shop & multiplex",
                "price": "500 Sq. Ft.* Onwards"
            },
            {
                "category": "Crore",
                "img_src": 'images/crore3.jpg',
                "title": "M3M IFC",
                "description": "Sector 66, Gurugram ",
                 "description1": "Retail Spaces ",
                "price": " 1500 Sq. Ft.* Onwards"
            },
            {
                "category": "Crore",
                "img_src": 'images/crore4.jpg',
                "title": "M3M SKY Lofts",
                "description": "Sector 71, Gurugram ",
                 "description1": "Service Apartments ",
                "price": " 800 Sq. Ft.* Onwards"
            }
            
        ]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            contact = form.save(commit=False)
            # Access the form data here
            print(contact)
            # Save the contact to the database
            contact.save()
            # return redirect('contact_success')
            
        else:
            print(form.errors)
            
            # form = ContactForm()
        # return render(request, 'home.html', { 'cards':cards,'form': form})
    else:
        form = ContactForm()
        # print(form)
        
        
    return render(request,  'home.html', {'cards':cards,'form': form})