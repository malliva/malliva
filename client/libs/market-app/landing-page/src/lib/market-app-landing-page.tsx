import React from 'react';

import './market-app-landing-page.module.scss';
import { MarketAppTopMenu } from 'libs/market-app/top-menu/src/index';
import { MarketAppSignUps } from 'libs/market-app/sign-ups/src/index';
import { MarketAppSignIn } from 'libs/market-app/sign-in/src/index';

/* eslint-disable-next-line */
export interface MarketAppLandingPageProps {}

export function MarketAppLandingPage(props: MarketAppLandingPageProps) {
  return (
    <div>
      <MarketAppTopMenu />
      {/* <MarketAppSignUps /> */}
      <MarketAppSignIn />
    </div>
  );
}

export default MarketAppLandingPage;
