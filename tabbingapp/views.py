from django.http import HttpResponse
from django.shortcuts import render_to_response

def about(request):
    return HttpResponse("<h3><br><br><br><br>Tabbing app is an initiative to create a platform for easier and accurate tabulation <br>of scores and teams for national and international debate tournaments.<br> It creates match ups for teams based on their performance and allocates<br> them rooms and judges for all rounds of the tournament and <br>updates their scores accordingly to announce winners.<br>The broad aim is to reduce human errors and the time taken to<br> manually take care of scores by directly providing a link to participants<br> and judges for the updation of scores without the involvement of organizers.<br><br><br><br>Click back button to revisit the website</h3>")

def home(request):
    return render_to_response('home.html')