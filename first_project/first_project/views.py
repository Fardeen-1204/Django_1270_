from django.shortcuts import HttpResponse

def hello(request):
    # return HttpResponse("<center><h1>Hii from batch no 1270</h1></center>")
    return HttpResponse("""<center><table border="2">
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table> </center>""")
def home(request):
    return HttpResponse("<center><h1>This is home page</h1></center>")