/*  Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js */

let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#AAB7C4'
        }
    },
    invalid: {
        color: '#DC3545',
        iconColor: '#DC3545'
    }
};

let card = elements.create('card', {style: style});
card.mount('#card-element');

// Handles realtime validation errors on the card element
card.addEventListener('change', function(event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html =
            `<span><i class="far fa-times-circle"></i></span>
            <span class="ml-1">${event.error.message}</span>`
        ;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});