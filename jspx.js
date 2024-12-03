// ==UserScript==
// @name         上海市教师教育培训
// @match        *://jspx.21shte.net/*
// ==/UserScript==

(function () {
  window.anyInterval = setInterval(function () {
    const videoElement = document.querySelector("video");
    if (videoElement) {
      videoElement.muted = true;
      videoElement.playbackRate = 15.0;

      var targetText = $(
        "#blk_learn_nav > div > div.pull-right.text-right > span.t > span.clock"
      )
        .text()
        .trim();
      if (targetText === "已满足本单元所需的学习时间") {
        var topics = $(".topic");

        var activeIndex = topics.index($(".topic.active"));

        if (activeIndex !== -1 && activeIndex < topics.length - 1) {
          var nextTopic = topics.eq(activeIndex + 1);
          nextTopic.click();
        } else {
          console.log("这是最后一课");
        }
      } else {
        console.log("学习时间未满足条件");
      }

      videoElement.play().catch((error) => {
        console.error("OHNO:", error);
      });
    } else {
      console.log("没有视频，好卡");
    }
  }, 500);
})();
