import React from 'react';

import './market-app-landing-page.module.scss';
import { MarketAppTopMenu } from 'libs/market-app/top-menu/src/index';

/* eslint-disable-next-line */
export interface MarketAppLandingPageProps {}

export function MarketAppLandingPage(props: MarketAppLandingPageProps) {
  return (
    <div>
      <MarketAppTopMenu />
    </div>
  );
}

export default MarketAppLandingPage;
