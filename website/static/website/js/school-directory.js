

var all_states = [...new Set($.map(schools, function(school) {
    return school.state;
}))].sort();


$(document).ready(function(){

    
    $(".state-name-loader").click(function(){ 
        stateLoading();
    
    })

       $(document).on('click', '.each-state-name', function(){
        extension = $(this).attr("id-modifier")
        let first_list = ''; // Initialize an empty string for the list
        
        let selected_state = $(this).text(); // Get the clicked state's text
        
        // Filter schools based on selected state
        let filtered_states = schools.filter(obj => obj.state === selected_state);
        
        // Use a Set to ensure unique cities
        let uniqueCities = new Set(filtered_states.map(single_state => single_state.city));
        
        // Check if any unique cities are found
        if (uniqueCities.size === 0) {
            first_list = '<li>No list found</li>';
            // =================show the choice placeholder here==================
        } else {
            // Loop through the unique cities and build the HTML list items
            uniqueCities.forEach(city => {
                first_list += '<li class="area-list">' + city + '</li>'; // Add city to the list
            });
        }
        
        // Append the list to the #found-state element
        // $('#found-state').  // Use .html() to append HTML

            $("#lg-list-"+extension).html(first_list);
            $('.each-state-name').hide()
            $('.each-state-lg').hide()
            $(this).show()

            $("#lg-list-"+extension).show();
            $("#found-schools").text("")


       })

    // =======================to return a list of areas in the selected state =======================

       $(".state-name-filter").click(function() {
        let first_list = ''; // Initialize an empty string for the list
        
        let selected_state = $(this).text(); // Get the clicked state's text
        
        // Filter schools based on selected state
        let filtered_states = schools.filter(obj => obj.state === selected_state);
        
        // Use a Set to ensure unique cities
        let uniqueCities = new Set(filtered_states.map(single_state => single_state.city));
        
        // Check if any unique cities are found
        if (uniqueCities.size === 0) {
            first_list = '<li>No schools found</li>';
        } else {
            // Loop through the unique cities and build the HTML list items
            uniqueCities.forEach(city => {
                first_list += '<li class="list-of-cities">' + city + '</li>'; // Add city to the list
            });
        }
        
        // Append the list to the #found-state element
        $('#found-state').html(first_list);  // Use .html() to append HTML

    });
    
    
    // =======================to return list of single schools in the area =======================
    $(document).on("click", ".area-list", function(){

            schools_in_area = ""
            let selected_area = $(this).text()
            filtered_schools = schools.filter(obj => obj.city === selected_area)
            
            for (single_school of filtered_schools){
                schools_in_area += '<p href="#school_name" class="single-school">'+ single_school.school_name + '</p>'
            }
            
            $(".area-list").hide()
            $(this).show()
            $("#found-schools").html(schools_in_area)
     
       })

    // =======================to return a single school from the list of schools in the area =======================

       $(document).on("click", ".single-school", function(){
        selected_school = $(this).text()
        // target_school = schools.filter(obj => (obj.School_name === selected_school))
        let target_school = schools.find(obj => obj.school_name === selected_school);
        

        serial= target_school.serial
        school_name= selected_school
        ownership= target_school.ownership
        nursery= target_school.nursery
        primary= target_school.primary
        junior= target_school.junior
        senior= target_school.senior
        address= target_school.address
        area= target_school.area
        city= target_school.city
        lga= target_school.lga
        state= target_school.state
        email= target_school.email
        telephone= target_school.telephone
        website= target_school.website
        faith= target_school.faith
        hostel= target_school.hostel
        gender= target_school.gender
        bus= target_school.bus
        airconditioning= target_school.airconditioning 
        library= target_school.library
        sports_arena= target_school.sports_arena
        science_laboratory= target_school.science_laboratory
        ict_studio= target_school.ict_studio
        tuck_shop= target_school.tuck_shop
        primary_6= target_school.primary_6
        sickbay= target_school.sickbay
        
$("#serial").text(serial)
$("#school_name").text(school_name)
$("#ownership").val(ownership)
$("#nursery").val(nursery)
$("#primary").val(primary)
$("#junior").val(junior)
$("#senior").val(senior)
$("#address").text(address)
$("#area").text(area)
$("#city").text(city)
$("#lga").text(lga)
$("#state").text(state)
$("#email").text(email)
$("#telephone").text(telephone)
$("#website ").text(website)
$("#faith").val(faith)
$("#hostel").val(hostel)
$("#gender").val(gender)
$("#bus").val(bus)
$("#airconditioning").val(airconditioning)
$("#library").val(library)
$("#sports_arena").val(sports_arena)
$("#science_laboratory").val(science_laboratory)
$("#ict_studio").val(ict_studio)
$("#tuck_shop").val(tuck_shop)
$("#primary_6").val(primary_6)
$("#sickbay").val(sickbay)

        // $(".Contact-School").show()
        $(".business-search-result").show();
        $("#correct-details").show()
        $(".state-name-details").hide();

        
    })
});





function clearResults (){ 
            $("#id").text("")
            $("#School_name").text("")
            // $("#ownership").text("")
            // $("#Nursery").text("")
            // $("#Primary").text("")
            // $("#Junior_Secondary").text("")
            // $("#Senior_Secondary").text("")
            $("#Address_line_1").text("")
            $("#Address_line_2").text("")
            $("#Address_line_3").text("")
            $("#City").text("")
            $("#Area").text("")
            $("#lga").text("")
            $("#State").text("")
            // $(".Contact-School").show()
            // $(".business-search-result").hide()
            // $("#correct-details").hide()

}
function stateLoading (){ 
    state_names = all_states
    listed_states = ""
    for(i=0; i< state_names.length; i++){
        listed_states += `<p class="each-state-name" id-modifier="${i}">${state_names[i]}</p>
        <li class="each-state-lg" id="lg-list-${i}" style="display: none;">
        
        </li>`
        // alert(state_names[i])
    }

        $("#all-state-names").html(listed_states);
        $("#found-schools").text("");
        // $(".school-search-container").hide();
        $(".state-name-details").show();
        $(".business-search-result").text("")
        $("#correct-details").hide()
        $(".Contact-School").hide()

   
}
