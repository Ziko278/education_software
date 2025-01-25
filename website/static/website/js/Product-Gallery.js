  /*---------- Product Image Gallery ----------*/
    // Delegate event to dynamically added images
    $(document).on("click", ".change-btns img", function() {
        var productImage = $(".product-des .image");
        var productMain = $(".main img");

        // Active Button
        $(".change-btns img.active").removeClass("active"); // Remove the "active" class from the currently active button
        $(this).addClass("active"); // Add the "active" class to the clicked button to mark it as active

        // Active Image
        var src = $(this).attr("src"); // Get the source attribute of the clicked thumbnail image
        productMain.attr("src", src); // Update the source attribute of the main product image to display the clicked image
    });