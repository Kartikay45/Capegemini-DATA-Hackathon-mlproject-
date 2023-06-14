/**
 * Define a function to navigate betweens form steps.
 * It accepts one parameter. That is - step number.
 */
const navigateToFormStep = (stepNumber) => {
    /**
     * Hide all form steps.
     */
    document.querySelectorAll(".form-step").forEach((formStepElement) => {
        formStepElement.classList.add("d-none");
    });
    /**
     * Mark all form steps as unfinished.
     */
    document.querySelectorAll(".form-stepper-list").forEach((formStepHeader) => {
        formStepHeader.classList.add("form-stepper-unfinished");
        formStepHeader.classList.remove("form-stepper-active", "form-stepper-completed");
    });
    /**
     * Show the current form step (as passed to the function).
     */
    document.querySelector("#step-" + stepNumber).classList.remove("d-none");
    /**
     * Select the form step circle (progress bar).
     */
    const formStepCircle = document.querySelector('li[step="' + stepNumber + '"]');
    /**
     * Mark the current form step as active.
     */
    formStepCircle.classList.remove("form-stepper-unfinished", "form-stepper-completed");
    formStepCircle.classList.add("form-stepper-active");
    /**
     * Loop through each form step circles.
     * This loop will continue up to the current step number.
     * Example: If the current step is 3,
     * then the loop will perform operations for step 1 and 2.
     */
    for (let index = 0; index < stepNumber; index++) {
        /**
         * Select the form step circle (progress bar).
         */
        const formStepCircle = document.querySelector('li[step="' + index + '"]');
        /**
         * Check if the element exist. If yes, then proceed.
         */
        if (formStepCircle) {
            /**
             * Mark the form step as completed.
             */
            formStepCircle.classList.remove("form-stepper-unfinished", "form-stepper-active");
            formStepCircle.classList.add("form-stepper-completed");
        }
    }
};
/**
 * Select all form navigation buttons, and loop through them.
 */
document.querySelectorAll(".btn-navigate-form-step").forEach((formNavigationBtn) => {
    /**
     * Add a click event listener to the button.
     */
    formNavigationBtn.addEventListener("click", () => {
        /**
         * Get the value of the step.
         */
        const stepNumber = parseInt(formNavigationBtn.getAttribute("step_number"));
        /**
         * Call the function to navigate to the target form step.
         */
        navigateToFormStep(stepNumber);
    });
});

//calculations
// area=cotton(hectares/acres)
// rainfall=region(cm)
// lime=cotton(tonnes)
// urea=cotton(tonnes)

// fraclime=1
// purity of limestone(p)=0.9
// emission factor for limestone(ef)=0.12
// cg=3.67

function co2_emi_from_cotton_lime() {
    var num1 = parseFloat(document.getElementById("lime").value);
var fraclime = 1;
var pu = 0.9;
var ef = 0.12;
var cg = 3.67;
    var result1 = (num1*fraclime*pu*ef) + ((num1*(1-fraclime)*pu*ef))*cg;
    document.getElementById("ccl").innerHTML = result1;
  }

// ef=0.20
// c=3.67

  function co2_emi_from_cotton_urea() {
    var num2 = parseFloat(document.getElementById("quantity").value);
var ef1 = 0.20;
var c1 = 3.67;
    var result2 = num2*ef1*c1;
    document.getElementById("ccfu").innerHTML = result2;
  }



  function n20_emi_from_cotton() {
    var num3 = parseFloat(document.getElementById("quantity").value);
    var num4 = parseFloat(document.getElementById("area").value);
var cos1 = 0.46;
var cos2 = 1.57;
var cos3 = 0.0055;
var cos4 = 265;
var cos5 = 0.001;
    var result3 = num3*cos1*num4*cos2*cos3*cos4*cos5;
    document.getElementById("ncfu").innerHTML = result3;
  }