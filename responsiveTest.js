describe('Responsive Test of browser', () => {
    it('TestCase : Responsive Test in desktop', async () => {
        await browser.setWindowSize(1366, 768)
        await browser.url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        await $("//input[@name='username']").setValue('Admin')
        await $("//input[@name='password']").setValue('admin123')
        await $('//button[@type="submit"]').click();
        await browser.pause(2000);
        await browser.saveScreenshot('browserDesktop.png')
        await $('//p[@class="oxd-userdropdown-name"]').click(); 
        await $('//a[contains(text(),"Logout")]').click();
        await browser.pause(2000)
    })
    it('TestCase : Responsive Test in Ipad', async () => {
        await browser.setWindowSize(820, 1180)
        await browser.url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        await $("//input[@name='username']").setValue('Admin')
        await $("//input[@name='password']").setValue('admin123')
        await $('//button[@type="submit"]').click() 
        await browser.pause(2000);
        await browser.saveScreenshot('browserIpad.png')
        await $('//p[@class="oxd-userdropdown-name"]').click(); 
        await $('//a[contains(text(),"Logout")]').click();
        await browser.pause(2000)
    })
    it('TestCase : Responsive Test in Iphone', async () => {
        await browser.setWindowSize(390, 844)
        await browser.url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        await $("//input[@name='username']").setValue('Admin')
        await $("//input[@name='password']").setValue('admin123')
        await $('//button[@type="submit"]').click() 
        await browser.pause(2000);
        await browser.saveScreenshot('browserIpad.png')
        await $('//img[@class="oxd-userdropdown-img"]').click(); 
        await $('//a[contains(text(),"Logout")]').click();
        await browser.pause(2000)
    })
})