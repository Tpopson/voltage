var cartbtn = document.querySelector('#create-btn');
var form = document.querySelector('#form');



form.addEventListener('submit', function(e){
    e.preventDefault()
    var cartdata = new FormData()
    cartdata.append('proid', document.querySelector('#proid').value)
    cartdata.append('quant', document.querySelector('#quant').value)
    cartdata.append('csrfmiddlewaretoken', '{{csrf_token}}')
    axios.post('/addtocart/', cartdata)
        .then(function(resp){
            if(resp.data.status === 'success'){
                cartbtn.click()  
                form.reset()
            }
        })
        .catch(function(err){
            console.log(err)
        })
});





// def pay(request):
//     pid = request.POST.get('proid')
//     quanty = request.POST.get('quant')
//     try:
//         ShopCart.objects.create(quantity= quanty, price= pid)
//         resp = {
//             'status':'success'
//         }
//     except Exception as e:
//         print(e)
//         resp = {
//             'status':'failed'
//         }
//     return JsonResponse(resp)