import React from 'react';

import './market-app-landing-page.module.scss';
import { MarketAppTopMenu } from 'libs/market-app/top-menu/src/index';
import { MarketAppMainFilter } from 'libs/market-app/main-filter/src/index';
import { MarketAppItemList } from 'libs/market-app/item-list/src/index';
/* eslint-disable-next-line */
export interface MarketAppLandingPageProps {}

export function MarketAppLandingPage(props: MarketAppLandingPageProps) {
  return (
    <div>
      <MarketAppTopMenu />
      <div className="mt-10 grid grid-cols-1 gap-4 items-start lg:grid-cols-3 lg:gap-8">
        <div className="grid grid-cols-1 gap-4 lg:col-span-1">
          <MarketAppMainFilter />
        </div>
        <div className="grid grid-cols-1 gap-4 lg:col-span-2">
          <MarketAppItemList />
        </div>
      </div>
    </div>
  );
}

export default MarketAppLandingPage;
