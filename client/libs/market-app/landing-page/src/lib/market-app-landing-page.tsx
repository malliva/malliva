import React from 'react';

import './market-app-landing-page.module.scss';
import { MarketAppTopMenu } from 'libs/market-app/top-menu/src/index';
import { MarketAppMainFilter } from 'libs/market-app/main-filter/src/index';
import { MarketAppItemList } from 'libs/market-app/item-list/src/index';
import { MarketAppFooter } from 'libs/market-app/footer/src/index';
import { MarketAppTopBanner } from 'libs/market-app/top-banner/src/index';
import { MarketAppTopBarSettings } from 'libs/market-app/top-bar-settings/src/index';
/* eslint-disable-next-line */
export interface MarketAppLandingPageProps {}

export function MarketAppLandingPage(props: MarketAppLandingPageProps) {
  return (
    <div>
      <MarketAppTopMenu />
      <MarketAppTopBanner />
      {/* <MarketAppTopBarSettings /> */}
      <div className="flex justify-center space-between">
        <MarketAppMainFilter />
        <MarketAppItemList />
      </div>

      <MarketAppFooter />
    </div>
  );
}

export default MarketAppLandingPage;
