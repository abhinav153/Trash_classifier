
$(document).ready(function(){

//console.log('hello');

var btn = document.getElementById("button");

//console.log(btn);

//add event listener to btn
btn.addEventListener("click", function () {
     //console.log('added event listener to btn 1')

    var form = document.getElementById("files");
    console.log(form)
    var form_data = new FormData(form);
    $.ajax({
        	url: "/submit",
        	type: "post",
        	data: form_data,
        	contentType: false,
        	processData: false,
        	success : function(data) {
        		//alert('sucess');
        		prediction = data['class'];
        		document.getElementById("prediction").innerHTML = prediction;
        	},
        	error : function(data,error){
        		console.log(error);
        		prediction = data['class'];
        		console.log(data);
        		console.log(prediction);
        		document.getElementById("prediction").innerHTML = prediction;
        	}
        });
});

//console.log('added event listener to btn 2')



 


	
})



