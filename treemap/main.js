const horizontal=0;
const vertical=1;
let maxlength=1600;
let drawing  = document.getElementById("trmap")
let ctx = drawing.getContext("2d");
ctx.strokeStyle="#000000";
ctx.lineCap="round";
ctx.lineJoin="round";
ctx.linewidth=5;
ctx.strokeRect(10,10,1000,1000);

function basicRow(x1,y1,x2,y2,way,data)
{
    let len=data["sub"].length;
    let width=x2-x1;
    let height=y2-y1;


    let worst;
    let i=0,areaSum=0;
    let arr=Array();
    for(i=0;i<len;i++)
    {
        areaSum+=data["sub"][i].sum;
        arr.push(data["sub"][i].sum);
        arr.sort();
        let fix;
        if(way===horizontal)
        {
            fix=areaSum/height;
        }
        else
        {
            fix=areaSum/width;
        }
        let min=ratio(arr[0]/fix,fix);
        let max=ratio(arr[arr.length-1],fix);
        if(i==0)
        {
            worst=min;
            continue;
        }
        if(min >worst || max>worst)break;
        else
        {
            if(max>=min)worst=min;
            else worst=max;
        }
    }
    console.log("i=",i," areaSum= ",areaSum);
    return [i,areaSum];
}

function basicDraw(x1,y1,x2,y2,data)
{
    let len=data["sub"].length;
    let width=x2-x1;
    let height=y2-y1;
    let way;
    if(width>=height)way=vertical;
    else way=horizontal;
    let tmp=basicRow(x1,y1,x2,y2,(way+1)%2,data);
    let num=tmp[0];
    let areaSum=tmp[1];
    let x1_=x1,y1_=y1,x2_,y2_;
    if(way===vertical)
    {
        x2_=x1_+ areaSum/height;
        y2_=y2;

        for(let i=0;i<num;++i)
        {
            ctx.strokeRect(x1_,y1_,areaSum/height,(data["sub"][i].sum/areaSum)*height);
            console.log("areaSum=", areaSum,", height= ", height,", unit_area=",data["sub"][i].sum);
            y1_+= (data["sub"][i].sum/areaSum)*height;
        }


        for(let i=0;i<num;++i)
        {
            data["sub"].shift();
        }

    }
    else if(way===horizontal)
    {
        x2_=x2;
        y2_=y2+areaSum/width;

        for(let i=0;i<num;++i)
        {
            ctx.strokeRect(x1_,y1_,(data["sub"][i].sum/areaSum)*width,areaSum/width);
            x1_+= (data["sub"][i].sum/areaSum)*width;
        }

        for(let i=0;i<num;++i)
        {
            data["sub"].shift();
        }
    }



}


function  msg(e)
{
    let f=e.target.files[0];
    let reader=new FileReader();

    function lam_1()
    {
        function re(e)
        {
            let someThing = e.target.result;
            let dt=JSON.parse(someThing);
            basicDraw(0,0,1000,1000,dt);
        };
        return re;
    }
    reader.onload=lam_1(f);
    reader.readAsText(f);
}

function ratio(width,height)
{
    if(width>=height)return width/height;
    return height/width;
}

document.getElementById("select file").addEventListener("change", msg);
















