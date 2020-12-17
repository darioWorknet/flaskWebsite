function myFunction() {
    var myWidth = screen.width
    var heightFactor = 1.45;
    var pdfHeight = myWidth > 800 ?  800 * heightFactor : myWidth * heightFactor;
    var pixWidth = myWidth.toString() + "px";
    var pixHeight = pdfHeight.toString() + "px";

    document.getElementById("pdf-container").style.width = pixWidth;
    document.getElementById("pdf-container").style.height = pixHeight;
    console.log(pixWidth + " x " + pixHeight);
    console.log(" ");
  }

myFunction();

// Resize listener
window.onresize = myFunction;


