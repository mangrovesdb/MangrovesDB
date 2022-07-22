pragma solidity >=0.4.22 <0.9.0;

contract FlowControl {

  function calcDozenDiscountIf(uint purchasedQty) private pure returns (bool) {
    bool giveDozenPrice = false;

    if(purchasedQty >= 12){
      giveDozenPrice = true;
    } else {
      giveDozenPrice = false;
    }
    return (giveDozenPrice);
  }

  function calcDozenDiscountWhile(uint purchasedQty) private pure returns (bool) {
    bool giveDozenPrice = false;
    uint numDonuts = 1;

    while (numDonuts < purchasedQty) {
      numDonuts++;
      if (numDonuts >= 12) {
        giveDozenPrice = true;
        break;
      }
    }
    return (giveDozenPrice);
  }

  function calcDozenDiscountDo(uint purchasedQty) private pure returns (bool) {
    bool giveDozenPrice = false;
    uint numDonuts = 1;

    do{
      numDonuts ++;
      if(numDonuts >= 12) {
        giveDozenPrice = true;
        break;
      }
    } while(numDonuts < purchasedQty);
    return (giveDozenPrice);
  }

  function calcDozenDiscountFor(uint purchasedQty) private pure returns (bool) {
    bool giveDozenPrice = false;
    uint numDonuts = 1;

    for(numDonuts = 1; numDonuts <= purchasedQty; numDonuts++){
      if(numDonuts >= 12){
        giveDozenPrice = true;
        break;
      }
    }
    return(giveDozenPrice);
  }
}