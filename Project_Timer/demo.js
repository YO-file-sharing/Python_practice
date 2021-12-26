var monthText=["01月","02月","03月","04月","05月","06月","07月","08月","09月","10月","11月","12月"];
var dayText=["01日","02日","03日","04日","05日","06日","07日","08日","09日","10日","11日","12日","13日","14日","15日","16日","17日","18日","19日","20日","21日","22日","23日","24日","25日","26日","27日","28日","29日","3日","31日"];
var weekText=["日曜日","月曜日","火曜日","水曜日","木曜日","金曜日","土曜日"];
var hourText=["00時","01時","02時","03時","04時","05時","06時","07時","08時","09時","10時","11時","12時","13時","14時","15時","16時","17時","18時","19時","20時","21時","22時","23時"];
var minuteText=["01分","02分","03分","04分","05分","06分","07分","08分","09分","10分","11分","12分","13分","14分","15分","16分","17分","18分","19分","20分","21分","22分","23分","24分","25分","26分","27分","28分","29分","30分","31分","32分","33分","34分","35分","36分","37分","38分","39分","40分","41分","42分","43分","44分","45分","46分","47分","48分","49分","50分","51分","52分","53分","54分","55分","56分","57分","58分","59分","60分"];
var secondsText=["01秒","02秒","03秒","04秒","05秒","06秒","07秒","08秒","09秒","10秒","11秒","12秒","13秒","14秒","15秒","16秒","17秒","18秒","19秒","20秒","21秒","22秒","23秒","24秒","25秒","26秒","27秒","28秒","29秒","30秒","31秒","32秒","33秒","34秒","35秒","36秒","37秒","38秒","39秒","40秒","41秒","42秒","43秒","44秒","45秒","46秒","47秒","48秒","49秒","50秒","51秒","52秒","53秒","54秒","55秒","56秒","57秒","58秒","59秒","60秒"];
var clock;var monthList=[];
var dayList=[];
var weekList=[];
var hourList=[];
var minuteList=[];
var secondsList=[];
var isCircle=false;
var textSet=[[monthText,monthList],
[dayText,dayList],
[weekText,weekList],
[hourText,hourList],
[minuteText,minuteList],
[secondsText,secondsList]];
window.onload=function()
{
 init();
 setInterval(function()
 {runTime();
 },100);
 changePosition();
 setTimeout(function()
 {changeCircle();
 },2000);
}
function init()
{clock=document.getElementById('clock');
for(var i=0;
 i<textSet.length;i++)
 {for(var j=0;j<textSet[i][0].length;j++)
 {var temp=createLabel(textSet[i][0][j]);
 clock.appendChild(temp);textSet[i][1].push(temp);
 }
 }
}
function createLabel(text)
{
 var div=document.createElement('div');
div.classList.add('label');
div.innerText=text;return div;
}
function runTime()
{
 var now=new Date();
 var month=now.getMonth();
 var day=now.getDate();
 var week=now.getDay();
 var hour=now.getHours();
 var minute=now.getMinutes();
 var seconds=now.getSeconds();
 initStyle();
 var nowValue=[month,day-1,week,hour,minute,seconds];
 for(var i=0;
 i<nowValue.length;
 i++)
 {var num=nowValue[i];
 textSet[i][1][num].style.color='#000000'; //ハイライトカラー
 }
if(isCircle)
{var widthMid=document.body.clientWidth/2;
 var heightMid=document.body.clientHeight/2;
 for(var i=0;
 i<textSet.length;
 i++){for(var j=0;
 j<textSet[i][0].length;
 j++){var r=(i+1)*35+50*i;
 var deg=360/textSet[i][1].length*(j-nowValue[i]);
 var x=r*Math.sin(deg*Math.PI/180)+widthMid;
 var y=heightMid-r*Math.cos(deg*Math.PI/180);
 var temp=textSet[i][1][j];
 temp.style.transform='rotate('+(-90+deg)+'deg)';
 temp.style.left=x+'px';
 temp.style.top=y+'px';
 }
 }
 }
}
function initStyle()
{var label=document.getElementsByClassName('label');
for(var i=0;
 i<label.length;i++)
 {label[i].style.color='#d68bd6'; //ハイライトではない文字カラー
}
}
function changePosition()
{
 for(let i=0;i<textSet.length;
 i++)
 {
 for(let j=0;
 j<textSet[i][1].length;
 j++){
 let tempX=textSet[i][1][j].offsetLeft+"px";
 let tempY=textSet[i][1][j].offsetTop+"px";
 setTimeout(function(){
 textSet[i][1][j].style.position="absolute";
 textSet[i][1][j].style.left=tempX;textSet[i][1][j].style.top=tempY;
 },50);
 }
 }
 }
function changeCircle()
{
 isCircle=true;
 clock.style.transform="rotate(90deg)";
}
