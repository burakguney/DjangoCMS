﻿/*
 Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or http://ckeditor.com/license
*/
CKEDITOR.dialog.add("docProps",function(g){function p(a,d){var e=function(){b(this);d(this,this._.parentDialog)},b=function(a){a.removeListener("ok",e);a.removeListener("cancel",b)},f=function(a){a.on("ok",e);a.on("cancel",b)};g.execCommand(a);if(g._.storedDialogs.colordialog)f(g._.storedDialogs.colordialog);else CKEDITOR.on("dialogDefinition",function(b){if(b.data.name==a){var d=b.data.definition;b.removeListener();d.onLoad=CKEDITOR.tools.override(d.onLoad,function(a){return function(){f(this);d.onLoad=
a;"function"==typeof a&&a.call(this)}})}})}function l(){var a=this.getDialog().getContentElement("general",this.id+"Other");a&&("other"==this.getValue()?(a.getInputElement().removeAttribute("readOnly"),a.focus(),a.getElement().removeClass("cke_disabled")):(a.getInputElement().setAttribute("readOnly",!0),a.getElement().addClass("cke_disabled")))}function i(a,d,e){return function(b,f,c){f=k;b="undefined"!=typeof e?e:this.getValue();!b&&a in f?f[a].remove():b&&a in f?f[a].setAttribute("content",b):b&&
(f=new CKEDITOR.dom.element("meta",g.document),f.setAttribute(d?"http-equiv":"name",a),f.setAttribute("content",b),c.append(f))}}function j(a,d){return function(){var e=k,e=a in e?e[a].getAttribute("content")||"":"";if(d)return e;this.setValue(e);return null}}function m(a){return function(d,e,b,f){f.removeAttribute("margin"+a);d=this.getValue();""!==d?f.setStyle("margin-"+a,CKEDITOR.tools.cssLength(d)):f.removeStyle("margin-"+a)}}function n(a,d,e){a.removeStyle(d);a.getComputedStyle(d)!=e&&a.setStyle(d,
e)}var c=g.lang.docprops,h=g.lang.common,k={},o=function(a,d,e){return{type:"hbox",padding:0,widths:["60%","40%"],children:[CKEDITOR.tools.extend({type:"text",id:a,label:c[d]},e||{},1),{type:"button",id:a+"Choose",label:c.chooseColor,className:"colorChooser",onClick:function(){var b=this;p("colordialog",function(d){var e=b.getDialog();e.getContentElement(e._.currentTabId,a).setValue(d.getContentElement("picker","selectedColor").getValue())})}}]}},q="javascript:void((function(){"+encodeURIComponent("document.open();"+
(CKEDITOR.env.ie?"("+CKEDITOR.tools.fixDomain+")();":"")+'document.write( \'<html style="background-color: #ffffff; height: 100%"><head></head><body style="width: 100%; height: 100%; margin: 0px">'+c.previewHtml+"</body></html>' );document.close();")+"})())";return{title:c.title,minHeight:330,minWidth:500,onShow:function(){for(var a=g.document,d=a.getElementsByTag("html").getItem(0),e=a.getHead(),b=a.getBody(),f={},c=a.getElementsByTag("meta"),h=c.count(),i=0;i<h;i++){var j=c.getItem(i);f[j.getAttribute(j.hasAttribute("http-equiv")?
"http-equiv":"name").toLowerCase()]=j}k=f;this.setupContent(a,d,e,b)},onHide:function(){k={}},onOk:function(){var a=g.document,d=a.getElementsByTag("html").getItem(0),e=a.getHead(),b=a.getBody();this.commitContent(a,d,e,b)},contents:[{id:"general",label:h.generalTab,elements:[{type:"text",id:"title",label:c.docTitle,setup:function(a){this.setValue(a.getElementsByTag("title").getItem(0).data("cke-title"))},commit:function(a,d,e,b,c){c||a.getElementsByTag("title").getItem(0).data("cke-title",this.getValue())}},
{type:"hbox",children:[{type:"select",id:"dir",label:h.langDir,style:"width: 100%",items:[[h.notSet,""],[h.langDirLtr,"ltr"],[h.langDirRtl,"rtl"]],setup:function(a,d,e,b){this.setValue(b.getDirection()||"")},commit:function(a,d,e,b){(a=this.getValue())?b.setAttribute("dir",a):b.removeAttribute("dir");b.removeStyle("direction")}},{type:"text",id:"langCode",label:h.langCode,setup:function(a,d){this.setValue(d.getAttribute("xml:lang")||d.getAttribute("lang")||"")},commit:function(a,d,e,b,c){c||((a=this.getValue())?
d.setAttributes({"xml:lang":a,lang:a}):d.removeAttributes({"xml:lang":1,lang:1}))}}]},{type:"hbox",children:[{type:"select",id:"charset",label:c.charset,style:"width: 100%",items:[[h.notSet,""],[c.charsetASCII,"us-ascii"],[c.charsetCE,"iso-8859-2"],[c.charsetCT,"big5"],[c.charsetCR,"iso-8859-5"],[c.charsetGR,"iso-8859-7"],[c.charsetJP,"iso-2022-jp"],[c.charsetKR,"iso-2022-kr"],[c.charsetTR,"iso-8859-9"],[c.charsetUN,"utf-8"],[c.charsetWE,"iso-8859-1"],[c.other,"other"]],"default":"",onChange:function(){this.getDialog().selectedCharset=
"other"!=this.getValue()?this.getValue():"";l.call(this)},setup:function(){this.metaCharset="charset"in k;var a=j(this.metaCharset?"charset":"content-type",1,1).call(this);!this.metaCharset&&a.match(/charset=[^=]+$/)&&(a=a.substring(a.indexOf("=")+1));if(a){this.setValue(a.toLowerCase());if(!this.getValue()){this.setValue("other");var d=this.getDialog().getContentElement("general","charsetOther");d&&d.setValue(a)}this.getDialog().selectedCharset=a}l.call(this)},commit:function(a,d,e,b,c){c||(b=this.getValue(),
c=this.getDialog().getContentElement("general","charsetOther"),"other"==b&&(b=c?c.getValue():""),b&&!this.metaCharset&&(b=(k["content-type"]?k["content-type"].getAttribute("content").split(";")[0]:"text/html")+"; charset="+b),i(this.metaCharset?"charset":"content-type",1,b).call(this,a,d,e))}},{type:"text",id:"charsetOther",label:c.charsetOther,onChange:function(){this.getDialog().selectedCharset=this.getValue()}}]},{type:"hbox",children:[{type:"select",id:"docType",label:c.docType,style:"width: 100%",
items:[[h.notSet,""],["XHTML 1.1",'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'],["XHTML 1.0 Transitional",'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'],["XHTML 1.0 Strict",'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'],["XHTML 1.0 Frameset",'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">'],
["HTML 5","<!DOCTYPE html>"],["HTML 4.01 Transitional",'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">'],["HTML 4.01 Strict",'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'],["HTML 4.01 Frameset",'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">'],["HTML 3.2",'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">'],["HTML 2.0",'<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">'],[c.other,
"other"]],onChange:l,setup:function(){if(g.docType&&(this.setValue(g.docType),!this.getValue())){this.setValue("other");var a=this.getDialog().getContentElement("general","docTypeOther");a&&a.setValue(g.docType)}l.call(this)},commit:function(a,d,c,b,f){f||(a=this.getValue(),d=this.getDialog().getContentElement("general","docTypeOther"),g.docType="other"==a?d?d.getValue():"":a)}},{type:"text",id:"docTypeOther",label:c.docTypeOther}]},{type:"checkbox",id:"xhtmlDec",label:c.xhtmlDec,setup:function(){this.setValue(!!g.xmlDeclaration)},
commit:function(a,d,c,b,f){f||(this.getValue()?(g.xmlDeclaration='<?xml version="1.0" encoding="'+(this.getDialog().selectedCharset||"utf-8")+'"?>',d.setAttribute("xmlns","http://www.w3.org/1999/xhtml")):(g.xmlDeclaration="",d.removeAttribute("xmlns")))}}]},{id:"design",label:c.design,elements:[{type:"hbox",widths:["60%","40%"],children:[{type:"vbox",children:[o("txtColor","txtColor",{setup:function(a,d,c,b){this.setValue(b.getComputedStyle("color"))},commit:function(a,d,c,b,f){if(this.isChanged()||
f)b.removeAttribute("text"),(a=this.getValue())?b.setStyle("color",a):b.removeStyle("color")}}),o("bgColor","bgColor",{setup:function(a,d,c,b){a=b.getComputedStyle("background-color")||"";this.setValue("transparent"==a?"":a)},commit:function(a,d,c,b,f){if(this.isChanged()||f)b.removeAttribute("bgcolor"),(a=this.getValue())?b.setStyle("background-color",a):n(b,"background-color","transparent")}}),{type:"hbox",widths:["60%","40%"],padding:1,children:[{type:"text",id:"bgImage",label:c.bgImage,setup:function(a,
d,c,b){a=b.getComputedStyle("background-image")||"";a="none"==a?"":a.replace(/url\(\s*(["']?)\s*([^\)]*)\s*\1\s*\)/i,function(a,b,d){return d});this.setValue(a)},commit:function(a,d,c,b){b.removeAttribute("background");(a=this.getValue())?b.setStyle("background-image","url("+a+")"):n(b,"background-image","none")}},{type:"button",id:"bgImageChoose",label:h.browseServer,style:"display:inline-block;margin-top:10px;",hidden:!0,filebrowser:"design:bgImage"}]},{type:"checkbox",id:"bgFixed",label:c.bgFixed,
setup:function(a,d,c,b){this.setValue("fixed"==b.getComputedStyle("background-attachment"))},commit:function(a,d,c,b){this.getValue()?b.setStyle("background-attachment","fixed"):n(b,"background-attachment","scroll")}}]},{type:"vbox",children:[{type:"html",id:"marginTitle",html:'<div style="text-align: center; margin: 0px auto; font-weight: bold">'+c.margin+"</div>"},{type:"text",id:"marginTop",label:c.marginTop,style:"width: 80px; text-align: center",align:"center",inputStyle:"text-align: center",
setup:function(a,d,c,b){this.setValue(b.getStyle("margin-top")||b.getAttribute("margintop")||"")},commit:m("top")},{type:"hbox",children:[{type:"text",id:"marginLeft",label:c.marginLeft,style:"width: 80px; text-align: center",align:"center",inputStyle:"text-align: center",setup:function(a,d,c,b){this.setValue(b.getStyle("margin-left")||b.getAttribute("marginleft")||"")},commit:m("left")},{type:"text",id:"marginRight",label:c.marginRight,style:"width: 80px; text-align: center",align:"center",inputStyle:"text-align: center",
setup:function(a,d,c,b){this.setValue(b.getStyle("margin-right")||b.getAttribute("marginright")||"")},commit:m("right")}]},{type:"text",id:"marginBottom",label:c.marginBottom,style:"width: 80px; text-align: center",align:"center",inputStyle:"text-align: center",setup:function(a,c,e,b){this.setValue(b.getStyle("margin-bottom")||b.getAttribute("marginbottom")||"")},commit:m("bottom")}]}]}]},{id:"meta",label:c.meta,elements:[{type:"textarea",id:"metaKeywords",label:c.metaKeywords,setup:j("keywords"),
commit:i("keywords")},{type:"textarea",id:"metaDescription",label:c.metaDescription,setup:j("description"),commit:i("description")},{type:"text",id:"metaAuthor",label:c.metaAuthor,setup:j("author"),commit:i("author")},{type:"text",id:"metaCopyright",label:c.metaCopyright,setup:j("copyright"),commit:i("copyright")}]},{id:"preview",label:h.preview,elements:[{type:"html",id:"previewHtml",html:'<iframe src="'+q+'" style="width: 100%; height: 310px" hidefocus="true" frameborder="0"></iframe>',onLoad:function(){var a=
this.getElement();this.getDialog().on("selectPage",function(c){if("preview"==c.data.page){var e=this;setTimeout(function(){var b=a.getFrameDocument(),c=b.getElementsByTag("html").getItem(0),d=b.getHead(),g=b.getBody();e.commitContent(b,c,d,g,1)},50)}});a.getAscendant("table").setStyle("height","100%")}}]}]}});