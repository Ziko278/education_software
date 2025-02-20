$(document).ready(function() {
    // Product Data Array
    productLoad = [

        {
            "product number": "52020112",
            "Product-group": "Uniform",
            "Product-Title": "School Uniforms",
            "new-price": "5500",
            "old-price": "6500",
            "details": "Kids will be kids, and playtime is always part of the fun! But with all that running around, uniforms get dirty fast. Say goodbye to fading and endless washes—our uniforms are built to stand the test of time! Durable, long-lasting, and ready for every adventure!",
            "description": "Our school essentials are designed with care, using carefully selected fabrics that prioritize comfort, durability, and breathability. From soft, cozy cardigans and pullovers to breathable sportswear, we choose materials that keep kids comfortable all day long. Stylish shorts, pinafores, blazers, and polished ties are made from fabrics that combine both functionality and a smart appearance. Our durable, soft socks in various lengths complete the uniform, ensuring every piece is made with the utmost attention to quality.",
            "max": "500",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        },
        {
            "product number": "52020103",
            "Product-group": "Portal",
            "Product-Title": "School Management Portal",
            "new-price": "500 per term",
            "old-price": "30000",
            "details": "Reduce costs by cutting paper usage and streamlining administrative tasks. A school management portal boosts efficiency through automation, real-time data access, and seamless communication, which enhances productivity and resource management overall.",
            "description": "Key features include a centralized dashboard, student information management, attendance tracking, grading and assessment tools, fee management, and event scheduling. It also offers secure messaging, automated report generation, and mobile compatibility. The portal enhances efficiency, transparency, and accessibility, enabling easy access to academic performance, school updates, and parent-teacher communication, while ensuring data security and role-based access.",
            "max": "4",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        },
        {
            "product number": "52020117",
            "Product-group": "Books",
            "Product-Title": "Children's Books",
            "new-price": "1300",
            "old-price": "3000",
            "details": "Unlock a world of adventure with great children's books. From magical journeys to thrilling quests, each story sparks imagination and creativity. Let your child’s imagination find flight as they dive into exciting worlds, meeting unforgettable characters and learning valuable lessons.",
            "description": "Whether you're building a school library, outfitting a home collection, or purchasing books for children, our selection features a variety of captivating reading materials. Popular titles include the *Diary of a Wimpy Kid* series, classic works by Dr. Seuss, Enid Blyton’s timeless stories, and many other engaging books that spark imagination and foster a lifelong love of reading.",
            "max": "445",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        },
        {
            "product number": "52020107",
            "Product-group": "CCTV",
            "Product-Title": "CCTV",
            "new-price": "80000",
            "old-price": "70000",
            "details": "Boost your school's security with our advanced CCTV cameras—delivering clear HD footage, motion detection, remote access, and 24/7 monitoring. Safeguard students, staff, and property, anytime, anywhere. Stay protected, stay smart.",
            "description": "This advanced CCTV system for schools offers real-time surveillance with high-definition cameras, providing clear footage day and night. Equipped with motion detection and smart analytics, it ensures enhanced security by alerting staff to any suspicious activity. The system supports remote access, allowing administrators to monitor live feeds from any location. With robust data encryption and cloud storage, footage is securely stored and easily accessible, promoting a safe learning environment for students and staff.",
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
            "details": "Academic gowns uphold tradition, fostering unity during key ceremonies like graduations. They add formality, allowing students and faculty to celebrate achievements with dignity, creating a professional atmosphere for a memorable experience.",
            "description": "Our academic gown is made from durable, comfortable fabric with a classic, flowing design. It features long sleeves and an open-front style, perfect for formal ceremonies. Available in traditional black and any other colours on request, it pairs with a cap and tassel for a professional, polished look at graduations and academic events.",
            "max": "4",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        },
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
            "Product-group": "Website",
            "Product-Title": "School Website",
            "new-price": "40000",
            "old-price": "30000",
            "details": "A  website defines a school's brand, improves communication with students, parents, and the community, and serves as a hub for schedules, announcements, and events, boosting visibility, online learning, and engagement.",
            "description": "Our website provide for creating online communities and forums, allowing parents to interact, share information, and engage with school activities. These features provide a safe environment, protected from the vulnerabilities of social media platforms, with robust encryption and security measures to ensure privacy. Parents can discuss topics, ask questions, and collaborate without concerns about data breaches or hacking, fostering stronger connections within the school community. Additionally, the website can include event updates, announcements, and resources, enhancing overall communication.",
            "max": "4",
            "Material": "not available",
            "Size": "not available",
            "Weight": "not available"
        }


    ];

    // Initialize empty string for the catalog HTML
    let buildCatalogue = "";

    // Get the number of products for sale
    let forSale = 3;

    // Loop through the productLoad array to build the catalog
    for (let i = 0; i < forSale; i++) {
        buildCatalogue += `
            <div class="product-item">
                <div class="image">
                    <img src="/static/website/images/Shop/Products/${productLoad[i]["Product-group"]}/Product-1.jpg" alt="${productLoad[i]["Product-Title"]}"> <!-- Product Image -->
                    <div class="options">
                        <!-- <a href="Wishlist.html" class="icon"><i class="fas fa-paper-plane"></i></a>Add to Wishlist Button -->
                        <a class="icon"><i class="fas fa-file-invoice  quote-button" Image-link="${productLoad[i]["Product-Title"]}"></i></a><!-- Quotation Button -->
                        <a class="icon"><i Image-link="${productLoad[i]["Product-group"]}"
                              new-price ="${productLoad[i]["new-price"]}"
                              old-price ="${productLoad[i]["old-price"]}"
                              details ="${productLoad[i]["details"]}"
                              description ="${productLoad[i]["description"]}"
                              max ="${productLoad[i]["max"]}"
                              Material ="${productLoad[i]["Material"]}"
                              Size ="${productLoad[i]["Size"]}"
                              Weight ="${productLoad[i]["Weight"]}"
                        
                        class="fa-solid fa-magnifying-glass Examine-Item"></i></a><!-- Product Detail Page Button -->
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
                    <div ><h3 Image-link="${productLoad[i]["Product-group"]}"
                              new-price ="${productLoad[i]["new-price"]}"
                              old-price ="${productLoad[i]["old-price"]}"
                              details ="${productLoad[i]["details"]}"
                              description ="${productLoad[i]["description"]}"
                              max ="${productLoad[i]["max"]}"
                              Material ="${productLoad[i]["Material"]}"
                              Size ="${productLoad[i]["Size"]}"
                              Weight ="${productLoad[i]["Weight"]}"

                    class="Examine-Item">${productLoad[i]["Product-Title"]}</h3></div> <!-- Product Title -->
                    <p>${productLoad[i].details}</p> <!-- Product Details -->
                    <div class="price">From: &#x20A6;${productLoad[i]["new-price"]} <span></span></div> <!-- Product Price -->
                </div>
            </div>`;
    }

    // Append the generated HTML to the container with id 'catalogue'
    $("#catalogue").html(buildCatalogue);

    let popularList = "";
    let listSize = productLoad.length;

    for (i=3; i< listSize; i++){
        popularList += `    <div class="post-item">
          <img src="/static/website/images/Shop/Products/${productLoad[i]["Product-group"]}/Product-3.jpg" alt="${productLoad[i]["Product-Title"]}"> <!-- Product Image -->
          <div class="content">
          <a ><h3 Image-link="${productLoad[i]["Product-group"]}"
          new-price ="${productLoad[i]["new-price"]}"
          old-price ="${productLoad[i]["old-price"]}"
          details ="${productLoad[i]["details"]}"
          description ="${productLoad[i]["description"]}"
          max ="${productLoad[i]["max"]}"
          Material ="${productLoad[i]["Material"]}"
          Size ="${productLoad[i]["Size"]}"
          Weight ="${productLoad[i]["Weight"]}"
          class="Examine-Item">${productLoad[i]["Product-Title"]}</h3></a> <!-- Product Title -->

            <div class="price">
            </div>
            </div>
        </div>
    `;
    }

    $("#Popular-Products") .html(popularList);
    

});
