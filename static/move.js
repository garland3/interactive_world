function set_canvas_to_full_screen() {
    var canvas = document.getElementById('mycanvas');
    canvas.width = document.body.clientWidth; //document.width is obsolete
    canvas.height = document.body.clientHeight; //document.height is obsolete
}


var counter = -25;
function DrawBackGround(ctx, width, height) {
    // ctx.fillStyle="rgba(34,45,23,0.4)";
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, width, height);
}

// function moveRectangle() {
//     // get the canvas element using the DOM
//     var canvas = document.getElementById('mycanvas');
//     // Make sure we don't execute when canvas isn't supported
//     if (canvas.getContext) {
//         var ctx = canvas.getContext('2d');
//         DrawBackGround(ctx, canvas.width, canvas.height);
//         ctx.fillStyle = "red";
//         var boxSize = 25;
//         ctx.fillRect(counter, boxSize, boxSize, boxSize);

//         counter += 1
//         if (counter > canvas.width) counter = -boxSize;
//         requestAnimationFrame(moveRectangle);
//         ctx.restore();
//     } else {
//         alert('You need Safari or Firefox 1.5+ to see this demo.');
//     }
// }
var imgArrayGlobal = [];

// function preloadImg(imrulrarray){

//     imrulrarray.forEach(element => {
//         var mylocalimg = new Image();
//         mylocalimg.src  = element;
//         imgArrayGlobal.push(mylocalimg);
//         console.log('im printing my url:'+ element)
//     });
//     console.log("finished filling global array. ")
//     MoveImgs(imgArrayGlobal);
// }

function MoveImgs() {
    // console.log("running move imgs")
    // get the canvas element using the DOM
    var canvas = document.getElementById('mycanvas');
    // Make sure we don't execute when canvas isn't supported
    if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        DrawBackGround(ctx, canvas.width, canvas.height);

        var t = 0;
        imgArrayGlobal.forEach(animageObj =>{          
            animageObj.step() 
            ctx.drawImage(animageObj.imgobj,animageObj.getX(), animageObj.y);
            t+=150;
            // console.log("looping over images with t"+t)
        });

        // ctx.fillStyle = "red";
        var boxSize = 100;
        // ctx.fillRect(counter, boxSize, boxSize, boxSize);

        counter += 1
        if (counter > canvas.width) counter = -boxSize;
        requestAnimationFrame(MoveImgs);
        ctx.restore();
    } else {
        alert('You need Safari or Firefox 1.5+ to see this demo.');
    }
}

class AnimageImage{
    constructor(url){
        this.canvasWidth =  document.getElementById('mycanvas').width;
        this.url = url
        this.imgobj = new Image();
        this.imgobj.src = url;
        this.setRndStart();
        console.log("new animage img x, y is " +this.x + " "+ this.y)
        this.speed = Math.random()*5+0.8;
     
    };

    setStartingPosition(x,y){
        this.xstart = x;
        this.ystart = y;
        this.x = x;
        this.y = y;
    };

    setRndStart(){
        var canvas = document.getElementById('mycanvas');
        var x = Math.floor((Math.random() * canvas.width) + 1);

        // dont' let it go off the bottom or top
        var ratio = 0.9;
        var y =-Math.floor( canvas.height*(1-ratio))+Math.floor((Math.random() * canvas.height*ratio) + 1);
        this.setStartingPosition(x,y);
    }

    step(){
        this.x+=this.speed;
        if (this.x>this.canvasWidth){this.x  = -100;}
    }
    getX(){
        return Math.floor(this.x);
    }
}

function preLoadImages(imgs){
    imgs.forEach(imgurl =>{      
        imgArrayGlobal.push(new AnimageImage(imgurl));     
        console.log("Loading:"+imgurl)
    });
}

function Start(){    
    set_canvas_to_full_screen();  
    preLoadImages(imgs);
    console.log(imgs);
    MoveImgs()
}