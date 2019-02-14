document.addEventListener('DOMContentLoaded', function(){
 try{


    document.querySelector(".signup-btn").onclick = function (e){
      if(document.getElementsByName("password")[0].value != document.getElementsByName("confirm-password")[0].value)
      {
        document.querySelector(".signup_error").style.display = "block";
        e.preventDefault();
        return false;
      }
    };
}catch(e){}

  try{


    document.getElementsByName("password")[0].onkeyup = function()
    {
      document.querySelector(".signup_error").style.display = "none";
    };

    document.getElementsByName("confirm-password")[0].onkeyup = function()
    {
      document.querySelector(".signup_error").style.display = "none";
    };
  }catch(e){}


  try{
  //change price when the user change size of item
    document.querySelectorAll(".select-size").forEach(function(select){
      select.onchange = function(){

        //find topping price
        let item = document.URL;
        item = item.split("/");
        item = item[item.length-1];
        let previousElement = this.previousElementSibling;
        let topping_price = 0;
        if(item == "pizza")
        {
          let topping = previousElement;
          while(topping.className != "dropdown-menu"){
            topping = topping.nextElementSibling;
          }
          topping_price = checkTopping(topping) * 0.5;
        }

        previousElement.innerHTML = "$"+(parseFloat(this.value)+topping_price);
        previousElement.previousElementSibling.value = "$"+(parseFloat(this.value)+topping_price);

        //change the price input and size input
        let input_price =   previousElement.previousElementSibling;
        input_price.value = parseFloat(this.value)+topping_price;

        input_price.previousElementSibling.value = "small";

      };
    });
  }
  catch(e){}


  try{
    //change the price when user adds or remove a topping
     document.querySelectorAll(".topping").forEach(function(topping){
       topping.onchange = function (){
         if (checkTopping(topping.parentNode) > 4){
           this.checked = false;
           alert("sorry, we only allow 4 toppings");
         }
         else if(this.checked == true)
         {
           let parent = topping.parentNode;
           while(parent.className != "price"){
             parent = parent.previousElementSibling;
           };
           length = parent.innerHTML.length;
           let price = parseFloat(parent.innerHTML.slice(1, length)) + 0.5;
           parent.innerHTML = "$"+price;
         }

         else{
           let parent = topping.parentNode;
           while(parent.className != "price"){
             parent = parent.previousElementSibling;
           };
           length = parent.innerHTML.length;
           console.log(length);
           let price = parseFloat(parent.innerHTML.slice(1, length)) - 0.5;
           parent.innerHTML = "$"+price;
         }
       };
     });
  }catch(e){}


  //return of many toppings has been selected
  function checkTopping(div)
  {
    let checked = 0;
    let child = div.childNodes;
    for(let i=1; i < child.length; i++)
    {
      if(child[i].className == "topping"){
        if(child[i].checked)
        {
          checked+=1;
        }
      }
    }
    return checked;
  }

  try{

     $(".add_cart").each(function(form){

       $( this ).submit(function( event ) {
         event.preventDefault();
         let price = $(this).find(".price").text();
         let item = $(this).data("item");
         let id = $(this).data("id");
         let toppings = [];
         $(this).find(".topping").each(function(){
           if($(this).is(':checked')){
             toppings.push($(this).data("id"));
           }
         });

         price = price.substr(1);
         $.ajax({
           type:"POST",
           url:"/add_item/"+item+"/"+id,
           data:{
             csrfmiddlewaretoken:document.querySelector("input[name=csrfmiddlewaretoken]").value,
             price:price,
             toppings:JSON.stringify(toppings),
           },
           success:function(data){
             let success_message = $(".alert");
             success_message.css("display", "block");
             success_message.find("span").html(data.name + " was added to shopping cart");
            $(".content-placeholder").css("display", "block");
             // Grab the template script
             var theTemplateScript = $("#alert-handlebar").html();
             // Compile the template
             var theTemplate = Handlebars.compile(theTemplateScript);
             // Define our data object
             var context={
               "message": data.name + " was added to shopping cart"
             };
             // Pass our data to the template
             var theCompiledHtml = theTemplate(context);

             // Add the compiled html to the page
             $('.content-placeholder').html(theCompiledHtml);
           },
           failure:function(){
             alert("something went wrong, sorry");
           }
         });
       });
     });
  }catch(e){}

  try{
    document.querySelector(".close").onclick = function(){
      document.querySelector(".alert").style.display="none";

    };
  }catch(e){}

  try{
    document.querySelector("#place_order").onsubmit = function(e){
      e.preventDefault();
      $.ajax({
        type:"POST",
        url:"/place_order",
        data:{
          total_price:document.querySelector("#total_price").value,
          csrfmiddlewaretoken:document.querySelector("input[name=csrfmiddlewaretoken]").value,
        },
        success:function(data){
          alert(data.total);

        },
        failure:function(){
          alert("something went wrong, sorry");
        }
      });

    };

  } catch(e){}

  try{
    $(".remove-cart-link").each(function(){
      $(this).click(function(event){
        event.preventDefault();
        let item_price = $(this).parent().data("price");
        let table = $(this).parent().data("item");
        let id = $(this).parent().data("id");
        $(this).parent().parent().remove();
        let new_total_price = floatDec(floatDec($("#total_price").val()) - floatDec(item_price));
        new_total_price = Math.round(new_total_price * 100) / 100
        $.ajax({
          type:"POST",
          url:"/remove_item",
          data:{
            csrfmiddlewaretoken:document.querySelector("input[name=csrfmiddlewaretoken]").value,
            table:table,
            id:id,
          },
          success:function(data){
            $("#total_price").val(new_total_price);
            $(".price_display").text("$"+new_total_price);
          },
          failure:function(){
            alert("something wen wrong");
          }
        });


      });
    });
  }catch(e){}

  //convert string to float with precision
  function floatDec(string) {
      return (parseFloat(string).toPrecision(12));
  }
});
