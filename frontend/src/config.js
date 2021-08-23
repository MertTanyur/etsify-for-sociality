export var developmentMode = false;
function determineBase() {
    let result;
    if (developmentMode) {
        result = 'http://localhost:8081';
    } else {
        result = 'https://sociality4-sl6b2mo6eq-uc.a.run.app/';
    }
    return result;
}

export var BASE = determineBase();