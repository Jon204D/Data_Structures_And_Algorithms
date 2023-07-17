/**
 * Given a positive integer millis, write an asynchronous function that 
 * sleeps for millis milliseconds. It can resolve any value.
 */

/**
 * @param {number} millis
 */
async function sleep(millis) {
    let sleepPromise = new Promise(function (resolve) {
        setTimeout(() => resolve(), millis);
    });
    await sleepPromise;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */