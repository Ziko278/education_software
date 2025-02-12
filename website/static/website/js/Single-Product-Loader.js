$(document).ready(function() {

    $(document).on("click", ".Examine-Item", function(){
        productGroup = $(this).attr("Image-Link")
        // productGroup = $(this).attr("Product-group")
        productTitle = $(this).text()
        newPrice = $(this).attr("new-price")
        oldPrice = $(this).attr("old-price")
        details = $(this).attr("details")
        description = $(this).attr("description")
        max = $(this).attr("max")
        material = $(this).attr("Material")
        size = $(this).attr("Size")
        weight = $(this).attr("Weight")
// For this example, I'm setting the first product as the default to display on page load
    // var defaultProduct = productLoad[2]; // You can change this to any index
    // Populate the product details on page load
    // if (defaultProduct) {
        $("#Product-Name").text(productTitle);
        $("#Product-Price").html("&#x20A6;" + newPrice);
        $("#Product-New-Price").html("&#x20A6;" + oldPrice);
        $("#Product-Detail").text(details);
        $("#Product-Description").text(description);
        $("#Product-Material").text(material);
        $("#Product-Size").text(size);
        $("#Product-Weight").text(weight);
    // }

    // Dynamically generate the product images
    var btn1 = `<img class="active" src="/static/website/images/Shop/Products/${productGroup}/Product-1.jpg" alt="${productTitle}"> <!-- Product Image -->`;
    var btn2 = `<img src="/static/website/images/Shop/Products/${productGroup}/Product-2.jpg" alt="${productTitle}"> <!-- Product Image -->`;
    var btn3 = `<img src="/static/website/images/Shop/Products/${productGroup}/Product-3.jpg" alt="${productTitle}"> <!-- Product Image -->`;
    var btn4 = `<img src="/static/website/images/Shop/Products/${productGroup}/Product-4.jpg" alt="${productTitle}"> <!-- Product Image -->`;

    // Add images to the DOM
    $("#main-btn").html(btn1);
    $("#button-image1").html(btn1);
    $("#button-image2").html(btn2);
    $("#button-image3").html(btn3);
    $("#button-image4").html(btn4);

    var image1 = `<img src="/static/website/images/Shop/Products/${productGroup}/Product-4.jpg" alt="${productTitle}"> <!-- Product Image -->`;
    var image2 = `<img src="/static/website/images/Shop/Products/${productGroup}/Product-3.jpg" alt="${productTitle}"> <!-- Product Image -->`;
    

    // Add images to the DOM
    $("#image-1").html(image1);
    $("#image-2").html(image2);
   
    
    $(".resources-sections").hide();
    $("#quoted-item").text(productTitle);
    $(".product-single").show();
    


    });
    $(document).on("click", ".quote-button", function(){

        $(".resources-sections").hide();
        $(".product-single").hide();
        $(".quotation").show();
    
    });

    
    $(document).on("click", "#quote-back-button", function(){

        $(".resources-sections").show();
        $(".quotation").hide();
        $(".product-single").hide();

    
    });

});