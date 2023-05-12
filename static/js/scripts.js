/*!
* Start Bootstrap - Agency v7.0.11 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

   // 띠배너
    var bannerFunc = function(){
        $('.promotionBanner .btnClose').bind("click", function(){
            $('.promotionBanner').animate({height: 0}, 500);
        });
    };
    $(function($){
        bannerFunc();
    });

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    /* 최상단배너 하루동안 닫기  */
    jQuery(".main_top_banner .top_banner_box_inner .top_banner_close .icon").bind("click", function() {
		if(jQuery("#top_banner_box_cloase").is(":checked")){
			jQuery(".main_top_banner").slideUp("fast");
			setCookiem("top_banner_cookie", "top_banner_cookie", 1);
		 } else {
			jQuery(".main_top_banner").slideUp("fast");
		 }
    });

var main_top_banner_diplay = jQuery(".main_top_banner").attr("data-ez-display");
if (!getCookiem("top_banner_cookie") && (main_top_banner_diplay == 'visible')) {
	jQuery(".main_top_banner").slideDown("fast");
}

/*최상단배너 닫기버튼 없을시 높이 수정 */
if(jQuery(".top_banner_close").css("display") == "none"){
	jQuery(".main_top_banner").addClass('close_none');
	if (main_top_banner_diplay == 'visible') {
		jQuery(".main_top_banner").slideDown("fast");
	}
}




});



  