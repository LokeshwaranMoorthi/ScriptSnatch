// Update quantity and calculate total
function updateQuantity(medicine, change) {
    let qtyElement = document.getElementById(`qty_${medicine}`);
    let totalElement = document.getElementById(`total_${medicine}`);
    let grandTotalElement = document.getElementById('grand_total');

    let priceElement = totalElement.parentElement.querySelector('td:nth-child(2)');
    let price = parseFloat(priceElement.textContent.replace('Rs.', '').trim());

    let quantity = parseInt(qtyElement.textContent) + change;

    if (quantity >= 1) {
        qtyElement.textContent = quantity;
        totalElement.textContent = `Rs.${(price * quantity).toFixed(2)}`;
    } else {
        alert('Quantity cannot be less than 1.');
    }

    updateGrandTotal();
}

function updateGrandTotal() {
    let totalElements = document.querySelectorAll('[id^=total_]');
    let grandTotal = 0;

    totalElements.forEach(element => {
        let value = parseFloat(element.textContent.replace('Rs.', '').trim());
        if (!isNaN(value)) {
            grandTotal += value;
        }
    });

    document.getElementById('grand_total').textContent = `₹${grandTotal.toFixed(2)}`;
}

function placeOrder() {
    alert("Order placed successfully!");
}