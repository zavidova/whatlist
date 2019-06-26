

  var totalWidth;
  var totalHeight;
  var third;
  var mouseZone;
  var imgNumber;


  // Check Cursor Position
  $(window).on("mousemove", function(event) {

      // If it enters the Left Zone
      if ( event.pageX >= 0 && event.pageX < third ) {
        $(".red").css("mix-blend-mode", "multiply");
        $(".yellow").css("mix-blend-mode", "luminosity");
        $(".lilac").css("mix-blend-mode", "opacity");

      }

      // If it enters the Middle Zone
      else if (event.pageX >= third && event.pageX < third * 2) {
        $(".red").css("mix-blend-mode", "substract");
        $(".yellow").css("mix-blend-mode", "darken");
        $(".lilac").css("mix-blend-mode", "multiply");


      }

      // If it enters the Right Zone
      else if (event.pageX >= third * 2 && event.pageX < third * 3  ) {
        $(".red").css("mix-blend-mode", "screen");
        $(".yellow").css("mix-blend-mode", "multiply");
        $(".lilac").css("mix-blend-mode", "lighten");
    
      }

      // Update Screen Info
      $("#currentXPosition").html(event.pageX); $("#currentYPosition").html(event.pageY);
      $("#print").html(mouseZone);

  });

  // Update Variables and Screen Info when the screen size is changed
  $(window).resize(function() { checkSizes(); });
  jQuery(document).ready(function() { checkSizes(); });

  function checkSizes() {
      $("#currentXPosition").html("0"); $("#currentYPosition").html("0");
      totalWidth = $(window).width();
      totalHeight = $(window).height();
      third = totalWidth / 3;
      $("#widthValue").html(totalWidth);
      $("#heightValue").html(totalHeight);
  }






 
