

function changeMainTab(mainName) {
    document.querySelectorAll('.main-tab-content').forEach(div => {
        div.style.display = 'none';
    });

    const mainContent = document.getElementById(mainName + '-content');
    if (mainContent) mainContent.style.display = 'block';

    document.querySelectorAll('.main-tab-button').forEach(button => {
        button.classList.remove('active');
    });

    const mainButton = document.getElementById(mainName + '-button');
    if (mainButton) mainButton.classList.add('active');

    const firstSubButton = mainContent.querySelector('.sub-tab-button');
    if (firstSubButton) {
        const subName = firstSubButton.textContent.trim();
        changeSubTab(mainName, subName);
    }
}


function changeSubTab(mainName, subName) {
    const mainContent = document.getElementById(mainName + '-content');
    mainContent.querySelectorAll('.sub-tab-content').forEach(div => {
        div.style.display = 'none';
    });

    const subContent = document.getElementById(mainName + '-' + subName + '-content');
    if (subContent) subContent.style.display = 'block';

    mainContent.querySelectorAll('.sub-tab-button').forEach(subButton => {
        subButton.classList.remove('active');
    });

    const subButton = document.getElementById(mainName + '-' + subName + '-button');
    if (subButton) subButton.classList.add('active');
}