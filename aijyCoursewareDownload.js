javascript:(function(){try{const e=document.querySelector("#iframe_src");if(e){const t=e.getAttribute("src").match(/https:\/\/bjdownload\.cycore\.cn\S+\.(ppt|doc)(x?)/);if(t){const o=t[0],n=document.createElement("a");n.href=o,n.download="",document.body.appendChild(n),n.click(),document.body.removeChild(n)}else console.error("未找到有效的下载链接")}else console.error("未找到iframe元素")}catch(e){console.error("脚本运行出错",e)}})();
