var loadbtn = document.getAnimations('load_checkout');
var checkouttab = document.getAnimations('checkout');

// addbtn.addEventListener('click', () =>{
//     alert('clicked')
// })


loadbtn.addEventListener('click', function(){
    axios.get('/checkout/').then(function(resp){
        checkouttab.innerHTML = resp.date
    }).catch(function(err){
        console.log(err)
    })
});



// <!-- axios cdn  -->
/* <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/1.0.0-alpha.1/axios.min.js" integrity="sha512-xIPqqrfvUAc/Cspuj7Bq0UtHNo/5qkdyngx6Vwt+tmbvTLDszzXM0G6c91LXmGrRx8KEPulT+AfOOez+TeVylg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script> */
// <!-- axios cdn  -->