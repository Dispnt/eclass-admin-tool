// https://dolearning.net/school/subjects
// 全员学科组长，上传校本课程
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function clickButtons() {
    const totalTeachers = document.querySelectorAll("#inner-app > div.user-list.normal > div > div > span > div").length;//有几个老不死的东西

    for (let i = 1; i <= totalTeachers; i++) {
        let descriptionText = document.querySelector(`#inner-app > div.user-list.normal > div > div > span > div:nth-child(${i}) > div > div > div > div.ant-card-meta-detail > div.ant-card-meta-description > span`).innerText;
        if (descriptionText === "学科组长") {
            console.log(`跳过第 ${i} 个已经是组长`);
            continue;
        }
        document.querySelector(`#inner-app > div.user-list.normal > div > div > span > div:nth-child(${i}) > div > ul > li:nth-child(1) > span > button`).click();
        await delay(200);

        document.querySelector("div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(1) > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > span").click();
        await delay(200);
        document.querySelector(".ant-select-dropdown-content > ul > li:nth-child(2)").click();
        await delay(200);

        document.querySelector("div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary").click();
        await delay(200);
    }
}

clickButtons();
