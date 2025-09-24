// https://dolearning.net/school/subjects
// 全员学科组长，上传校本课程

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getElement(xpath, context = document) {
    return document.evaluate(xpath, context, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

async function setAllTeachersAsGroupLeaders() {
    const teacherCards = document.querySelectorAll(".user-list.normal .ant-card.ant-card-bordered");
    
    if (teacherCards.length === 0) {
        console.log("X 没有找到老师，要自己点开科目，看到一堆老师的页面。");
        return;
    }

    console.log(`总共找到 ${teacherCards.length} 个人...`);
    let processedCount = 0;

    for (const card of teacherCards) {
        const descriptionElement = card.querySelector(".ant-card-meta-description > span");
        const teacherName = card.querySelector('.ant-card-meta-title a')?.innerText || '未知姓名';

        if (!descriptionElement || descriptionElement.innerText.trim() === "学科组长") {
            console.log(`- [跳过] ${teacherName} ，已经是学科组长`);
            continue;
        }
        
        console.log(`▶ [处理中] ${teacherName} 现在还是 ${descriptionElement.innerText.trim()}`);
        processedCount++;

        const settingsButton = getElement(".//button[contains(., '修改权限')]", card);

        if (!settingsButton) {
            console.error(`  └ X [大的来了] 在 ${teacherName} 的卡片中没找到修改权限按钮。`);
            continue;
        }
        settingsButton.click();
        await delay(5000); 
        const dropdownTrigger = getElement("//div[contains(@class, 'ant-modal-body')]//div[contains(@class, 'ant-select-selection')]");
        if (!dropdownTrigger) {
            console.error("  └ X [大的来了] 没找到权限下拉菜单。");
            const closeButton = getElement("//div[contains(@class, 'ant-modal-content')]//button[@aria-label='Close']");
            if (closeButton) closeButton.click(); 
            await delay(500);
            continue;
        }
        dropdownTrigger.click();
        await delay(500); 
        const groupLeaderOption = getElement("//div[contains(@class, 'ant-select-dropdown') and not(contains(@class, 'ant-select-dropdown-hidden'))]//li[text()='学科组长']");
        if (!groupLeaderOption) {
            console.error("  └ X [大的来了] 没找到“学科组长”选项。");
            const closeButton = getElement("//div[contains(@class, 'ant-modal-content')]//button[@aria-label='Close']");
            if (closeButton) closeButton.click();
            await delay(500);
            continue;
        }
        groupLeaderOption.click();
        await delay(500);

        const confirmButton = getElement("//div[contains(@class, 'ant-modal-footer')]//button[span[text()='确 定']]");
        if (!confirmButton) {
            console.error("  └ X [大的来了] 没找到确定按钮。");
            const closeButton = getElement("//div[contains(@class, 'ant-modal-content')]//button[@aria-label='Close']");
            if (closeButton) closeButton.click();
            await delay(500);
            continue;
        }
        confirmButton.click();
        console.log(`  └ √ [拿下] ${teacherName} 的权限已修改。`);
        await delay(500); 
    }

    console.log(`▶ 结束，共deal了 ${processedCount} 位教师。`);
}

setAllTeachersAsGroupLeaders();