$(document).ready(function() {
    // Product Data Array
    productLoad = [
        {
            "product number": "52020101",
            "Product-group": "Solar",
            "Product-Title": "Solar For Schools",
            "new-price": "120000",
            "old-price": "30000",
            "details": "Customized solar electrification for schools provides reliable, sustainable energy solutions. Reduce electricity costs, enhance learning environments, and promote environmental responsibility with tailored solar systems, ensuring power for classrooms and school activities.",
            "description": "Customized solar electrification for schools provides reliable, sustainable energy solutions. Reduce electricity costs, enhance learning environments, and promote environmental responsibility with tailored solar systems, ensuring power for classrooms and school activities.",
            "max": "4",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        },
        {
            "product number": "52020102",
            "Product-group": "Portal",
            "Product-Title": "School Website",
            "new-price": "40000",
            "old-price": "30000",
            "details": "A school website is essential for communication, showcasing achievements, providing important updates, and fostering community engagement. Enhance your school's visibility, accessibility, and professionalism with an effective, easy-to-navigate website today!",
            "description": "A school website is essential for communication, showcasing achievements, providing important updates, and fostering community engagement. Enhance your school's visibility, accessibility, and professionalism with an effective, easy-to-navigate website today!",
            "max": "4",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        },
        {
            "product number": "52020103",
            "Product-group": "Website",
            "Product-Title": "School Management Portal",
            "new-price": "500 per term",
            "old-price": "30000",
            "details": "Our school management portal streamlines communication, simplifies administrative tasks, and enhances student performance tracking. With easy access to grades, schedules, and updates, it improves efficiency and fosters a connected school community.",
            "description": "Our school management portal streamlines communication, simplifies administrative tasks, and enhances student performance tracking. With easy access to grades, schedules, and updates, it improves efficiency and fosters a connected school community.",
            "max": "4",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        },
        {
            "product number": "52020104",
            "Product-group": "Gowns",
            "Product-Title": "Academic Gowns",
            "new-price": "6000",
            "old-price": "30000",
            "details": "Academic gowns that combine tradition with quality, providing students with a dignified and professional appearance for graduations and other school ceremonies. Tailored for comfort and prestige, ensuring a memorable academic milestone.",
            "description": "Academic gowns that combine tradition with quality, providing students with a dignified and professional appearance for graduations and other school ceremonies. Tailored for comfort and prestige, ensuring a memorable academic milestone.",
            "max": "4",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        }
    ];

    // Initialize empty string for the catalog HTML
    let buildCatalogue = "";

    // Get the number of products for sale
    let forSale = productLoad.length;

    // Loop through the productLoad array to build the catalog
    for (let i = 0; i < forSale; i++) {
        buildCatalogue += `
            <div class="product-item" style="margin-bottom:30px">
                <div class="image">
                    <img src="/static/website/images/Shop/Products/${productLoad[i]["Product-group"]}/Product-1.jpg" alt="${productLoad[i]["Product-Title"]}"> <!-- Product Image -->
                    <div class="options">
                        <!-- <a href="Wishlist.html" class="icon"><i class="fas fa-paper-plane"></i></a>Add to Wishlist Button -->
                        <a href="Quotation.html" class="icon"><i class="fas fa-file-invoice"></i></a><!-- Add to Cart Button -->
                        <a href="Product-Single/${productLoad[i]["Product-group"]}.html" class="icon"><i class="fa-solid fa-magnifying-glass"></i></a><!-- Product Detail Page Button -->
                    </div>
                </div>
                <div class="content">
                    <div class="rating"> <!-- Product Rating -->
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <a href="Product-Single/${productLoad[i]["Product-group"]}.html"><h3 class="Examine-Item">${productLoad[i]["Product-Title"]}</h3></a> <!-- Product Title -->
                    <p>${productLoad[i].details}</p> <!-- Product Details -->
                    <div class="price">From: &#x20A6;${productLoad[i]["new-price"]} <span></span></div> <!-- Product Price -->
                </div>
            </div>`;
    }

    // Append the generated HTML to the container with id 'dump-here'
    $("#dump-here").html(buildCatalogue);

    let popularList = "";

    for (i=0; i<3; i++){
        popularList += `    <div class="post-item">
          <img src="/static/website/images/Shop/Products/${productLoad[i]["Product-group"]}/Product-3.jpg" alt="${productLoad[i]["Product-Title"]}"> <!-- Product Image -->
          <div class="content">
            <a href="Product-Single/${productLoad[i]["Product-group"]}.html">${productLoad[i]["Product-Title"]}</a>
            <div class="price">
            </div>
          </div>
        </div>
    `;
    }

    $("#Popular-Products") .html(popularList);


});
